# LiTHe kods website

## Getting started

```
git clone git@github.com:lithekod/site-v2.git
cd site-v2
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
If you are using **fish**, use `source venv/bin/activate.fish` instead.

## Running locally
```
flask run
```

### Adding new pages
Add new markdown files to `website/pages/` representing a swedish and english
version of the page. Then add the endpoints to `website/__init__.py`.
