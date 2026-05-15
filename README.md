# ottospace-example-django-allauth

Minimal Django + `django-allauth` example wired to **OttoAuth** (`auth.ottospace.co`) as an OpenID Connect provider.

> Discovery: `https://auth.ottospace.co/.well-known/openid-configuration`

## Quick start

```bash
git clone https://github.com/moradothmanepro-OTTO/ottospace-example-django-allauth.git
cd ottospace-example-django-allauth
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Register a client at https://id.ottospace.co/dashboard/oidc-clients
# Redirect URI: http://localhost:8000/accounts/oidc/ottospace/login/callback/

cp .env.example .env
# Fill OTTOSPACE_CLIENT_ID, OTTOSPACE_CLIENT_SECRET, DJANGO_SECRET_KEY.

python manage.py migrate
python manage.py runserver
# Open http://localhost:8000 — click "Sign in with OttoSpace".
```

## Files

- [project/settings.py](./project/settings.py) — allauth config (~50 LOC of net new)
- [project/urls.py](./project/urls.py) — wires `/accounts/` to allauth (5 LOC)
- [manage.py](./manage.py) — Django entrypoint

## How it works

`allauth.socialaccount.providers.openid_connect` ships a generic OIDC provider that consumes the OttoAuth discovery doc. The `SOCIALACCOUNT_PROVIDERS["openid_connect"]["APPS"]` block declares OttoSpace as one app under that provider; allauth handles PKCE, state, token exchange, and userinfo automatically.

## License

MIT
