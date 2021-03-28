### Installation

1. Create python virtual environment
```shell
python -m venv venv
```

2. Install the dependencies
```shell
sudo apt-get install python3-sqlalchemy
pip install -r requirements.txt
npm install

# you may need to install PostCSS globally as well
# npm install --global postcss postcss-cli
```

3. Build flask assets
```shell
flask assets build
```

4. Create db
```shell
flask create-db
```

### Usage
Use following command to start server:
```shell
flask run
```
