**This template is properly separated by production settings and dev settings.**

```bash
export PROJECT_NAME={your_PROJECT_NAME}
django-admin startproject --template https://github.com/insung151/django-fast-template/archive/master.zip $PROJECT_NAME
cd $PROJECT_NAME
mv $PROJECT_NAME/settings/secret.json.py $PROJECT_NAME/settings/secret.json
echo "secret.json" >> .gitignore
```