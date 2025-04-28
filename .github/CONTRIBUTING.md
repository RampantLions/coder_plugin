<!-- BEGIN LiminalCognition LLC CONTRIBUTING.MD V0.0.1 BLOCK -->

# 🤝 Contributing to `coder_plugin`

First off, thank you for taking the time to contribute to `coder_plugin`!  
We welcome contributions of all kinds — bug fixes, new features, tests, documentation, and feedback.

---

## 📋 How to Contribute

1. **Fork** the repository: [RampantLions/coder_plugin](https://github.com/RampantLions/coder_plugin)
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes locally**.
4. **Add tests** for your changes under the `tests/` directory.
5. **Run linting and tests** to ensure your changes meet quality standards.
6. **Commit** your changes:
   ```bash
   git commit -m "Short description of your changes."
   ```
7. **Push** your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Open a Pull Request** (targeting the `dev` branch).

---

## 🛠️ Setting Up Local Development

You'll need:

- **Python 3.11+**
- **Git**
- **uv** (or **pdm** for alternative setup)

Set up your environment:

```bash
# Clone your fork
git clone git@github.com:YOUR_USERNAME/coder_plugin.git
cd coder_plugin

# Sync the environment
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

---

## 🧪 Running Tests and Linters

Before submitting a pull request:

```bash
# Run code checks
make check

# Run tests
make test

# (Optional) Run across multiple Python versions
tox
```

If you don't have all Python versions installed locally, the CI/CD pipeline will run this for you.

---

## 🧹 Code Style

- Follow **PEP8** and **black** formatting standards.
- Use **ruff** for linting and **mypy** for type checking.
- Ensure all public functions, methods, and classes have **clear docstrings**.

```bash
make format
make lint
```

---

<!-- github-only -->

## 🐛 Bug Reports

Found a bug? Please:

- Search existing [issues](https://github.com/RampantLions/coder_plugin/issues) to see if it’s already reported.
- If not, [open a new issue](https://github.com/RampantLions/coder_plugin/issues/new/choose) and provide:
  - Your operating system and version
  - Python version
  - Exact reproduction steps
  - Expected behavior vs. actual behavior

📎 **Tip:** Including logs, screenshots, and code snippets helps us resolve bugs faster.

---

## ✨ Feature Requests

Want to propose a new feature? Please:

- [Open a feature request issue](https://github.com/RampantLions/coder_plugin/issues/new/choose).
- Clearly explain:
  - The problem it solves
  - How it improves `coder_plugin`
  - If possible, suggest a basic design or usage example

---

## 📚 Documentation Contributions

Good documentation is critical!  
You can contribute by:

- Improving docstrings
- Clarifying README sections
- Writing guides, examples, or tutorials

---

## 🔒 Security Issues

Please do **NOT** open GitHub issues for security vulnerabilities.  
Instead, report them privately by contacting:

📧 **[liminal.cognition@gmail.com](mailto:liminal.cognition@gmail.com)**

We take security seriously and will respond promptly.

---

## 📦 Pull Request Guidelines

Before opening a Pull Request:

- Ensure tests and linters pass (`pdm run test`, `pdm run lint`).
- Update or add docstrings where appropriate.
- Add unit tests for new or changed functionality.
- Target your pull request against the `dev` branch, not `master`.
- Keep pull requests focused: smaller PRs are easier to review and merge.

📎 **Tip:** Reference related issues in your PR description using GitHub keywords like `Fixes #123`, `Closes #456`, etc.

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the [License](LICENSE).

---

Thank you again for helping make `coder_plugin` better! 🎉

<!-- END LiminalCognition LLC CONTRIBUTING.MD BLOCK -->
