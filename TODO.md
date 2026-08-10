# Task: Fix ImportError in accounts

## Steps
- [x] Update `accounts/urls.py` to match actual views in `views.py`
- [x] Update `accounts/tests.py` to match two-step OTP signup flow
- [x] Fix `recruiters/urls.py` (was incorrectly containing accounts content)
- [x] Run `python manage.py makemigrations accounts` to verify fix
- [x] Run `python manage.py test accounts` - all 4 tests pass
