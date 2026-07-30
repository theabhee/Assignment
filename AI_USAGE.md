# AI Usage & Development Log

## 1. Tools Used
- **Gemini** – used it while setting up Django, debugging architecture decisions, and figuring out terminal/syntax issues (especially PowerShell vs Linux commands).

## 2. Example Prompts I Used
- "first lets build the basic and then we can later work on that, i gave the algo give me how to build that"
- "before that here is my current situation asses it very carfully and the guide me step by step"

## 3. What I Accepted vs Rejected
- **Rejected:** It first suggested a more complex structure with separate service layers (`services.py`) and extra abstraction. Felt like overkill for this project.
- **Accepted:** Went with a simple, standard Django setup (`models.py`, `views.py`, `urls.py`) and put the auto-sorting box selection logic directly there instead of splitting it up further.

## 4. Mistakes I Ran Into & How I Fixed Them
- **PowerShell vs curl:** Regular `curl` commands (Linux-style) kept throwing `ParameterBindingException` in PowerShell. Fixed by switching to `Invoke-RestMethod` instead.
- **404 errors that made no sense:** Django kept giving `Page not found (404)` even though my urls.py looked right — turned out I just hadn't saved the file, so the changes weren't picked up. Saved it, reloader kicked in, fixed.
- **Typo that crashed the server:** Got `ModuleNotFoundError: No module named 'wareshouse'` — had misspelled "warehouse" in `INSTALLED_APPS`. Fixed the spelling.
- **Missing table error:** Got `OperationalError('no such table: warehouse_box')` when running queries. Forgot to run migrations after adding the app — ran `makemigrations warehouse` and `migrate` and it was fine.

## 5. How I Verified Things Worked
- Checked in `manage.py shell` that box dimensions entered in random order (like `15, 5, 10`) were actually getting normalized to `[5, 10, 15]` by the `save()` override — confirmed it was working correctly.
- Tested the API by sending a POST request with dimensions `4 × 9 × 14` and weight `10`, which needed 3D rotation matching to fit properly. It correctly skipped the smaller boxes and returned **Box C (Long)** as expected.
