# NF11 Academy — Learning Workflow

This guide records the practical workflow for learning Python on Android using Google Colab, GitHub and Notion, with ChatGPT as a tutor.

## 1. Write and run code in Google Colab
1. Open the lesson notebook in Google Colab on Android.
2. Write Python in a code cell and tap Run.
3. Read the output and fix errors. Attempt exercises yourself before asking for a full solution.
4. Keep passwords, API keys, tokens and personal information out of notebooks and repository history.

## 2. Save the notebook to GitHub
1. In Colab, choose **File → Save a copy in GitHub**.
2. Select the **nexforge11/Nexforge11-academy** repository and the appropriate branch.
3. Use a descriptive filename, e.g. `01-python-fundamentals/NF11_Lesson_01.ipynb`, when possible.
4. Confirm the save, then open GitHub and verify that the file exists and contains your latest work.
5. If the direct-save option fails, download the `.ipynb` file and upload it to the repository through GitHub as a fallback.

**Verified integration test:** Colab saved `Untitled0.ipynb` to the repository's main branch; ChatGPT independently fetched and verified that file. This test establishes direct saving, not automatic ongoing synchronisation. Subsequent edits must be saved again.

## 3. Record progress in Notion
Use the **AI & Python Development Academy — Learning Dashboard**:
- **Lessons:** lesson title, stage, status, GitHub link and notes.
- **Assessments:** checkpoint results and areas needing practice.
- **Portfolio Projects:** larger projects and their GitHub references.

At the end of each lesson, review your work and update Notion (manually or with ChatGPT through the connected Notion tool). A GitHub save alone does **not** update Notion automatically.

**Verified integration test:** ChatGPT updated the Lesson 01 Notion record with the Colab-to-GitHub result and then fetched it to confirm the saved change.

## 4. Lesson completion checklist
- Explain the new concept in your own words.
- Run the example and complete the practical exercise.
- Pass a short checkpoint or review.
- Save and verify the code in GitHub.
- Update the Notion lesson and assessment records.
- Record what was learned, common mistakes, homework and the next lesson.

Do not mark a lesson **Completed** just because it was discussed or a notebook was saved.

## Current checkpoint
- Stage 1: Python Fundamentals.
- Lesson 01 — Your First Python Program: **In Progress**.
- `print()` and strings checkpoint: **Passed**.
- Variables: introduced, practical exercise **not yet assessed**.
- GitHub notebook: [Untitled0.ipynb](https://github.com/nexforge11/Nexforge11-academy/blob/main/Untitled0.ipynb).
- Notion lesson: [Lesson 01](https://app.notion.com/p/3fd8c1343727813ca6cefe51c88a63af).

## Helpful links
- [GitHub Academy repository](https://github.com/nexforge11/Nexforge11-academy)
- [Notion Academy dashboard](https://app.notion.com/p/3fd8c1343727816d81ebdd4a2facd87b)
- [Google Colab](https://colab.research.google.com/)

**Privacy note:** If the GitHub repository is public, notebooks and commit history are visible to anyone. Never commit secrets, even for hobby projects.
