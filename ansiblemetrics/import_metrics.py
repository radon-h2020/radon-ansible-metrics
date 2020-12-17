# General metrics
from ansiblemetrics.general.lines_code import LinesCode
from ansiblemetrics.general.lines_blank import LinesBlank
from ansiblemetrics.general.lines_comment import LinesComment
from ansiblemetrics.general.num_conditions import NumConditions
from ansiblemetrics.general.num_decisions import NumDecisions
from ansiblemetrics.general.num_deprecated_keywords import NumDeprecatedKeywords
from ansiblemetrics.general.num_keys import NumKeys
from ansiblemetrics.general.num_math_operations import NumMathOperations
from ansiblemetrics.general.num_suspicious_comments import NumSuspiciousComments
from ansiblemetrics.general.num_tokens import NumTokens
from ansiblemetrics.general.text_entropy import TextEntropy

# Playbook scope
from ansiblemetrics.playbook.avg_play_size import AvgPlaySize
from ansiblemetrics.playbook.avg_task_size import AvgTaskSize
from ansiblemetrics.playbook.num_authorized_key import NumAuthorizedKey
from ansiblemetrics.playbook.num_blocks import NumBlocks
from ansiblemetrics.playbook.num_blocks_error_handling import NumBlocksErrorHandling
from ansiblemetrics.playbook.num_commands import NumCommands
from ansiblemetrics.playbook.num_deprecated_modules import NumDeprecatedModules
from ansiblemetrics.playbook.num_distinct_modules import NumDistinctModules
from ansiblemetrics.playbook.num_external_modules import NumExternalModules
from ansiblemetrics.playbook.num_fact_modules import NumFactModules
from ansiblemetrics.playbook.num_file_exists import NumFileExists
from ansiblemetrics.playbook.num_file_mode import NumFileMode
from ansiblemetrics.playbook.num_file_modules import NumFileModules
from ansiblemetrics.playbook.num_filters import NumFilters
from ansiblemetrics.playbook.num_ignore_errors import NumIgnoreErrors
from ansiblemetrics.playbook.num_imported_playbooks import NumImportedPlaybooks
from ansiblemetrics.playbook.num_imported_roles import NumImportedRoles
from ansiblemetrics.playbook.num_imported_tasks import NumImportedTasks
from ansiblemetrics.playbook.num_includes import NumIncludes
from ansiblemetrics.playbook.num_included_roles import NumIncludedRoles
from ansiblemetrics.playbook.num_included_tasks import NumIncludedTasks
from ansiblemetrics.playbook.num_included_vars import NumIncludedVars
from ansiblemetrics.playbook.num_lookups import NumLookups
from ansiblemetrics.playbook.num_loops import NumLoops
from ansiblemetrics.playbook.num_name_with_vars import NumNameWithVars
from ansiblemetrics.playbook.num_parameters import NumParameters
from ansiblemetrics.playbook.num_paths import NumPaths
from ansiblemetrics.playbook.num_plays import NumPlays
from ansiblemetrics.playbook.num_prompts import NumPrompts
from ansiblemetrics.playbook.num_regex import NumRegex
from ansiblemetrics.playbook.num_roles import NumRoles
from ansiblemetrics.playbook.num_tasks import NumTasks
from ansiblemetrics.playbook.num_unique_names import NumUniqueNames
from ansiblemetrics.playbook.num_uri import NumUri
from ansiblemetrics.playbook.num_vars import NumVars

general_metrics = {
    'lines_code': LinesCode,
    'lines_blank': LinesBlank,
    'lines_comment': LinesComment,
    'num_conditions': NumConditions,
    'num_decisions': NumDecisions,
    'num_deprecated_keywords': NumDeprecatedKeywords,
    'num_keys': NumKeys,
    'num_math_operations': NumMathOperations,
    'num_suspicious_comments': NumSuspiciousComments,
    'num_tokens': NumTokens,
    'text_entropy': TextEntropy
}

playbook_metrics = {
    'avg_play_size': AvgPlaySize,
    'avg_task_size': AvgTaskSize,
    'num_authorized_key': NumAuthorizedKey,
    'num_blocks': NumBlocks,
    'num_block_error_handling': NumBlocksErrorHandling,
    'num_commands': NumCommands,
    'num_deprecated_modules': NumDeprecatedModules,
    'num_distinct_modules': NumDistinctModules,
    'num_external_modules': NumExternalModules,
    'num_fact_modules': NumFactModules,
    'num_file_exists': NumFileExists,
    'num_file_mode': NumFileMode,
    'num_file_modules': NumFileModules,
    'num_filters': NumFilters,
    'num_ignore_errors': NumIgnoreErrors,
    'num_import_playbook': NumImportedPlaybooks,
    'num_import_role': NumImportedRoles,
    'num_import_tasks': NumImportedTasks,
    'num_include': NumIncludes,
    'num_include_role': NumIncludedRoles,
    'num_include_tasks': NumIncludedTasks,
    'num_include_vars': NumIncludedVars,
    'num_lookups': NumLookups,
    'num_loops': NumLoops,
    'num_names_with_vars': NumNameWithVars,
    'num_parameters': NumParameters,
    'num_paths': NumPaths,
    'num_plays': NumPlays,
    'num_prompts': NumPrompts,
    'num_regex': NumRegex,
    'num_roles': NumRoles,
    'num_tasks': NumTasks,
    'num_unique_names': NumUniqueNames,
    'num_uri': NumUri,
    'num_vars': NumVars
}
