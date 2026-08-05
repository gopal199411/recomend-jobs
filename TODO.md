# Resolve Terminal Issues

## Plan
1. Fix the `staticfiles.W004` warning by creating the missing `static/` directory.
2. Add JWT token endpoints (`/api/token/`, `/api/token/refresh/`) so users can authenticate.
3. Add a root API view at `/` so it doesn't return 404.
4. Fix the doubled `recommendations/` prefix in `jos_recommend/urls.py` so URLs are clean (`/api/recommendations/`, `/api/recommendations/generate/`).

## Steps
- [x] Create `static/` directory in project root
- [x] Add JWT token endpoints to `jobrecproject/urls.py`
- [x] Add a root API view and wire it to `/`
- [x] Fix doubled `recommendations/` prefix in `jos_recommend/urls.py`
- [x] Verify with `python manage.py check` and run a quick test
