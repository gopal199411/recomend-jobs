
# Fix Duplicate Model Conflicts (db_table overlap)

## Root Cause
`jos_recommend` (original monolithic app) has duplicate `Candidate`, `Resume`, `JobDescription` models that conflict with the dedicated `candidate/`, `resume/`, `job_description/` apps.

## Plan

### Step 1: Remove duplicate models from `jos_recommend/models.py`
- [x] Remove `Candidate`, `Resume`, `JobDescription` classes
- [x] Keep only `JobRecommendation` with updated ForeignKeys pointing to dedicated apps

### Step 2: Update `jos_recommend/` files to import from dedicated apps
- [x] `serializers.py` - import from `candidate.models`, `resume.models`, `job_description.models`
- [x] `views.py` - update imports
- [x] `filters.py` - import `JobDescription` from `job_description.models`
- [x] `signals.py` - import `JobDescription` from `job_description.models`
- [x] `services.py` - import from `job_description.models`
- [x] `tests.py` - import from dedicated apps

### Step 3: Add dedicated app URLs to root URL config
- [x] Include `candidate/urls.py`, `job_description/urls.py`, `resume/urls.py` in `jobrecproject/urls.py`

### Step 4: Verify the fix
- [x] Run `python manage.py makemigrations`
- [x] Run `python manage.py migrate`
- [x] Run `python manage.py test jos_recommend`

---

# Fix Missing Migrations (NodeNotFoundError)

## Root Cause
The `candidate`, `resume`, and `job_description` apps had no `migrations` folder/file, but `jos_recommend.0001_initial` depends on them. This caused `NodeNotFoundError` (missing `resume.0001_initial`, then `candidate.0001_initial`).

## Fix
- [x] Regenerated all migrations from current models:
  - `candidate/migrations/0001_initial.py` (Candidate model)
  - `job_description/migrations/0001_initial.py` (JobDescription model)
  - `resume/migrations/0001_initial.py` (Resume model, depends on candidate)
  - `jos_recommend/migrations/0001_initial.py` (JobRecommendation model, depends on candidate/resume/job_description)
- [x] Verified with `python manage.py showmigrations` (full graph consistent, no errors)
- [x] Verified with `python manage.py check` (No issues)
- [x] Applied all migrations with `python manage.py migrate` (all OK)
- [x] Confirmed `django_migrations` table populated with all app migrations

