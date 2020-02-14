# Python modules
import argparse
import json
import os
import sys
import yaml

from io import StringIO

from ansiblemetrics.main import MetricExtractor, LoadingError

# Own modules
from ansiblemetrics.import_metrics import general_metrics, playbook_metrics, tasks_metrics

def getParser():
    description='Extract metrics from Ansible scripts.\n\nIf no optional parameter is passed, the tool computes only the general metrics which are suitable for both playbooks and task files.'
    
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(action='store', dest='src', help='source file (playbook or tasks file) or directory')
    parser.add_argument(action='store', dest='dest', help='destination path to save results')
    parser.add_argument('-o', '--output', action='store_true', help='shows output')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')

    return parser

def __load_file(path):
    """ Returns a StringIO object representing the content of the file at <path>, if any; None otherwise """
    if not os.path.isfile(path):
        return None

    content = StringIO()
    with open(path, 'r') as file:
        for line in file.readlines():
            content.write(re.sub(r'\s{2,2}', '\\t', line).expandtabs(2))

    return content

def __load_dir(input_dir):
    """ 
    Find all yaml file in the input directory and return a dictionary of k:v pairs where k is the filepath and \
        the v the content of the file at that path 
    """
    
    dirs_stack = []

    for item in os.listdir(input_dir):
        dirs_stack.append(os.path.join(input_dir, item))

    yml_files = []

    while len(dirs_stack) > 0:
        item = dirs_stack.pop()

        if os.path.isfile(item):
            _, file_extension = os.path.splitext(item)

            if file_extension in ['.yml', '.yaml']:
                yml_files.append(item)
                
        elif os.path.isdir(item):
            for sub_item in os.listdir(item):
                dirs_stack.append(os.path.join(item, sub_item))

    scripts = {}

    for filepath in yml_files:
        scripts[filepath] = __load_file(filepath)

    return scripts    

def __load(input):
    if os.path.isfile(input):
        return {input: __load_file(input)}
    elif os.path.isdir(input):
        return __load_dir(input)

    return dict()

def __save_output(json_data, out_path):

    if not os.path.isfile(out_path):
        data = []
    else:
        with  open(out_path, 'r') as json_file:
            data = json.load(json_file)

    data.append(json_data)

    with open(out_path, 'w') as out_file:
        json.dump(data, out_file, sort_keys=True)


def cl():

    parser = getParser()

    # If no options show help message and exit
    if len(sys.argv[1:]) == 0:
        parser.parse_args(['--help'])

    args = parser.parse_args()
    
    extractor = MetricExtractor()

    scripts = __load(args.src)
    for filepath, script in scripts.items():

        try:
            metrics = extractor.run(script)
            metrics['filepath'] = filepath

            __save_output(metrics, args.dest)
            # Pretty-print json to screen
            if args.output:
                metrics2Json = json.dumps(metrics, indent=4, sort_keys=True)
                print(metrics2Json)

        except LoadingError:
            print('\033[91m' + 'Error: failed to load {}. Insert a valid file!'.format(filepath) + '\033[0m')
        except yaml.YAMLError:
            print('The input file is not a yaml file')
        except Exception:
            print('An unknown error has occurred')
            

if __name__ == "__main__":
    cl()

