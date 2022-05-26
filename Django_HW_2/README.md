# Django_HW_2


### Project Management Application

Imagine you are developing a project management application called PMProject. PMProject is an application that can track multiple projects, and each project can have multiple tasks associated with it. 


The following steps will help you complete your task:

1. Create a Django project called PMProject.
2. Create a Django app called PMApp.
3. Create two related model classes.

    - Project
        - name (CharField, use max_length and help_text)
        - creation_time (DateTimeField, use auto_now_add and help_text)
        - completion_time (DateTimeField, use null and help_text)
        
    - Task
        - title (CharField, use max_length and help_text)
        - description (TextField, use help_text)
        - time_estimate (IntegerField, use help_text)
        - completed (BooleanField, use default=False)
4. Create migration scripts and migrate the models' definitions to the database.

#### Additional Practices:
- Use __str__(self) method.
- Add relationship one-many in Task Model (Any project should have many tasks).
