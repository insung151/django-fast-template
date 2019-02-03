**This template is properly separated by production settings and dev settings.**

```bash
django-admin startproject --template https://github.com/insung151/django-fast-template/archive/master.zip {project_name}
cd {project_name}
mv {project_name}/settings/secret.json.py {project_name}/settings/secret.json
echo "secret.json" >> .gitignore
```