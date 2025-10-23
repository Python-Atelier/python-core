# 🤝 Contributing to Python Atelier

> **Join our collaborative Python learning atelier!**

Thank you for your interest in contributing to Python Atelier! This guide will help you understand how to contribute effectively, whether you're a student, educator, or developer.

---

## 🎯 Ways to Contribute

### **For Students:**

- ✅ Submit solutions to practice questions
- ✅ Improve existing solutions
- ✅ Report bugs or suggest improvements
- ✅ Share learning experiences
- ✅ Help review other solutions

### **For Educators/EdTech Companies:**

- ✅ Submit bulk student solutions
- ✅ Suggest new practice questions
- ✅ Provide feedback on question quality
- ✅ Share teaching methodologies
- ✅ Contribute to documentation

### **For Developers:**

- ✅ Fix bugs or issues
- ✅ Add new features
- ✅ Improve documentation
- ✅ Optimize code structure
- ✅ Add new topics or questions

---

## 🚀 Quick Start Guide

### **1. Fork the Repository**

```bash
# Fork on GitHub first, then clone
git clone https://github.com/Python-Atelier/python-core.git
cd python-core
```

### **2. Set Up Your Environment**

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (if any)
pip install -r requirements.txt
```

### **3. Create a Branch**

```bash
# For solutions
git checkout -b solution/question-1-variables

# For new features
git checkout -b feature/new-topic

# For bug fixes
git checkout -b fix/mermaid-graph-issue
```

### **4. Make Your Changes**

- Follow the coding standards
- Test your changes
- Update documentation if needed

### **5. Commit and Push**

```bash
git add .
git commit -m "feat: Add solution for question 1 - Variables"
git push origin your-branch-name
```

### **6. Create Pull Request**

- Go to your fork on GitHub
- Click "New Pull Request"
- Fill out the PR template
- Submit for review

---

## 📝 Pull Request Guidelines

### **PR Title Format:**

- `feat: Add solution for question 1 - Variables`
- `fix: Resolve mermaid graph rendering issue`
- `docs: Update contributing guidelines`
- `style: Format code according to PEP 8`

### **PR Description Template:**

```markdown
## 📋 Description

Brief description of your changes

## 🎯 Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Solution submission

## 📁 Files Changed

- `path/to/file1.py`
- `path/to/file2.md`

## ✅ Checklist

- [ ] Code follows PEP 8 style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated (if applicable)
- [ ] Documentation updated (if applicable)

## 🧪 Testing

Describe how you tested your changes

## 📸 Screenshots (if applicable)

Add screenshots for UI changes
```

---

## 🎓 Solution Submission Workflow

### **For Individual Students:**

1. **Choose a Question**

   ```bash
   # Browse topics and select a question
   cd 01_variables_and_data_types/
   # Read questions.md to find a question
   ```

2. **Create Solution Folder and File**

   ```bash
   # Create solutions folder if it doesn't exist
   mkdir -p solutions
   cd solutions/
   
   # Create your solution file
   touch question_1.py
   # Edit with your solution
   ```

3. **Test Your Solution**

   ```bash
   python question_1.py
   # Ensure it runs without errors
   ```

4. **Submit PR**
   ```bash
   git add .
   git commit -m "feat: Add solution for question 1 - Variables"
   git push origin solution/question-1
   # Create PR on GitHub
   ```

### **For EdTech Companies:**

1. **Create Company Branch**

   ```bash
   git checkout -b company-name-student-solutions
   ```

2. **Add All Solutions**

   ```bash
   # Create solution files for all students
   # Use standard naming: question_XX.py
   # Include student names in the file header
   ```

3. **Submit Bulk PR**
   ```bash
   git add .
   git commit -m "feat: Add student solutions from Company Name"
   git push origin company-name-student-solutions
   # Create PR with company name and student list
   ```

---

## 📋 Code Standards

### **Python Code:**

- Follow PEP 8 style guide
- Use type hints where applicable
- Add docstrings to functions/classes
- Keep functions focused and small
- Handle exceptions appropriately

### **Documentation:**

- Use clear, concise language
- Include examples where helpful
- Keep formatting consistent
- Update related files when needed

### **Commit Messages:**

- Use conventional commit format
- Be descriptive but concise
- Reference issues when applicable

---

## 🏆 Review Process

### **For Solutions:**

1. **Automated Checks**

   - Code formatting (black/flake8)
   - Syntax validation
   - Basic functionality tests

2. **Manual Review**

   - Code quality assessment
   - Correctness verification
   - Learning value evaluation

3. **Selection Criteria**
   - Best solution gets merged
   - Alternative approaches may be kept
   - Feedback provided to all contributors

### **For Features/Bug Fixes:**

1. **Code Review**

   - Technical correctness
   - Code quality and style
   - Performance considerations

2. **Testing**

   - Unit tests (if applicable)
   - Integration tests
   - Manual testing

3. **Documentation**
   - README updates
   - Code comments
   - User guides

---

## 🐛 Reporting Issues

### **Bug Report Template:**

```markdown
## 🐛 Bug Description

Clear description of the issue

## 🔄 Steps to Reproduce

1. Go to '...'
2. Click on '...'
3. See error

## 📱 Expected Behavior

What should happen

## ❌ Actual Behavior

What actually happens

## 💻 Environment

- OS: [e.g., macOS, Windows, Linux]
- Python Version: [e.g., 3.11]
- Browser: [if applicable]

## 📸 Screenshots

Add screenshots if applicable

## 🔍 Additional Context

Any other context about the problem
```

### **Feature Request Template:**

```markdown
## 💡 Feature Description

Clear description of the new feature

## 🎯 Problem Statement

What problem does this solve?

## 💭 Proposed Solution

How should this work?

## 🔄 Alternative Solutions

Any other approaches considered?

## 📋 Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
```

---

## 🤝 Community Guidelines

### **Be Respectful:**

- Provide constructive feedback
- Appreciate different approaches
- Help others learn and grow

### **Be Collaborative:**

- Share your knowledge
- Ask questions when needed
- Help review others' work

### **Be Patient:**

- Review process takes time
- Maintainers are volunteers
- Focus on learning and improvement

### **Be Professional:**

- Use appropriate language
- Follow project guidelines
- Respect intellectual property

---

## 📞 Getting Help

### **For Contributors:**

- Check existing documentation
- Search closed issues/PRs
- Ask questions in PR comments
- Join community discussions

### **For EdTech Companies:**

- Contact maintainers directly
- Request custom workflows
- Discuss bulk submission processes
- Schedule integration meetings

---

## 🏅 Recognition

### **Contributor Levels:**

- **🥉 Bronze:** First solution accepted
- **🥈 Silver:** 10+ solutions accepted
- **🥇 Gold:** 25+ solutions accepted
- **💎 Diamond:** 50+ solutions + community contributions

### **Recognition Methods:**

- Contributor hall of fame
- Special mentions in releases
- Invitation to maintainer team
- Speaking opportunities

---

## 📈 Success Metrics

Track your contribution impact:

- [ ] Solutions submitted
- [ ] Solutions accepted
- [ ] Issues reported
- [ ] Features contributed
- [ ] Documentation improved
- [ ] Community helped

---

## 🎯 Next Steps

1. **Read the Guidelines:** Understand the submission process
2. **Choose Your Contribution:** Pick what you want to work on
3. **Start Small:** Begin with simple solutions or fixes
4. **Get Feedback:** Learn from reviews and comments
5. **Keep Contributing:** Build momentum and expertise

---

## 🏷️ Labeling Your Pull Requests & Issues

- **Mandatory:** You must select at least one label when creating a PR or issue.
- **Available labels:** solution-submission, bug, enhancement, documentation, help wanted, question, review needed, good first issue, discussion, duplicate, invalid, wontfix, badge-eligible, and more.
- **Auto-labeling:** The system will automatically apply the `solution-submission` label to all new PRs. If your PR/issue is eligible for a badge, mention it in your description and the `badge-eligible` label will be added automatically.
- **Manual selection:** Please review and add any additional relevant labels to help maintainers and reviewers.

---

**Thank you for contributing to Python Dojo! 🐍✨**

Your contributions help make Python learning accessible and collaborative for everyone. Together, we're building the best Python practice resource in the world!
