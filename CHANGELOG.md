### 0.3.9 (Latest)
- Refactoring:
  * **StringIO no more required**. Now, the metrics take a **string as input**. 
  * num_import_playbook -> num_imported_playbooks and NumImportPlaybook -> NumImportedPlaybooks
  * num_import_role -> num_imported_roles and NumImportRole -> NumImportedRoles
  * num_import_tasks -> num_imported_tasks and NumImportTasks -> NumImportedTasks
  * num_include -> num_includes and NumInclude -> NumImportedRoles
  * num_include_role -> num_included_roles and NumIncludeRole -> NumIncludedRoles
  * num_include_tasks -> num_included_tasks and NumIncludeTasks -> NumIncludedTasks
  * num_include_vars -> num_included_vars and NumIncludeVars -> NumIncludedVars


### **0.3.7**, **0.3.8**
- Fixed cli usage. Refactoring

### **0.3.6**
- Bugfix: division-by-zero in avg_task_size.py

### **0.3.5**

- Fixed missing include in MANIFEST.in

### **0.3.4**

- Added parameter ***--omit-zero-metrics*** to omit metrics equal to 0.
- Metrics *NumUserInteraction* renamed to *NumPrompts*.
