<!-- BEGIN LiminalCognition LLC CONTRIBUTING.MD V0.0.5 BLOCK -->

<p>

</p>

<h2 align="center">coder_plugin</h2>

## Contributing to `coder_plugin`

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.



1.  Fork the Project, check out https://github.com/RampantLions/coder_plugin
2.  Create your Feature Branch
    (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request




You can contribute in many ways:

# Types of Contributions

## Report Bugs

Report bugs at https://github.com/RampantLions/coder_plugin/issues

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

## Fix Bugs

Look through the GitHub issues for bugs.
Anything tagged with "bug" and "help wanted" is open to whoever wants to implement a fix for it.

## Implement Features

Look through the GitHub issues for features.
Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

## Write Documentation

coder_plugin could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

## Submit Feedback

The best way to send feedback is to file an issue at https://github.com/RampantLions/coder_plugin/issues.

If you are proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

# Get Started!

Ready to contribute? Here's how to set up `coder_plugin` for local development.
Please note this documentation assumes you already have `uv` and `Git` installed and ready to go.

1. Fork the `coder_plugin` repo on GitHub.

2. Clone your fork locally:

```bash
cd <directory_in_which_repo_should_be_created>
git clone git@github.com:YOUR_NAME/coder_plugin.git
```

3. Now we need to install the environment. Navigate into the directory

```bash
cd coder_plugin
```

Then, install and activate the environment with:

```bash
uv sync
```

4. Install pre-commit to run linters/formatters at commit time:

```bash
uv run pre-commit install
```

5. Create a branch for local development:

```bash
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

6. Don't forget to add test cases for your added functionality to the `tests` directory.

7. When you're done making changes, check that your changes pass the formatting tests.

```bash
make check
```

Now, validate that all unit tests are passing:

```bash
make test
```

9. Before raising a pull request you should also run tox.
   This will run the tests across different versions of Python:

```bash
tox
```

This requires you to have multiple versions of python installed.
This step is also triggered in the CI/CD pipeline, so you could also choose to skip this step locally.

10. Commit your changes and push your branch to GitHub:

```bash
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

11. Submit a pull request through the GitHub website.

# Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the feature to the list in `README.md`.


# 📋 Contributing

## coder_plugin: coder_plugin

We welcome contributions to **Coder Plugin**!

Please follow these guidelines:

---

### 🛠 Development Setup

- Use **Python 3.11**.
- Install dependencies via `hatch` or `uv`.

```bash
hatch env create
hatch run test
```

---

### 🧪 Testing

Run tests before submitting:

```bash
hatch run test
```

---

### 🧹 Code Style

Ensure code is formatted:

```bash
hatch run format
hatch run lint
```

Follow PEP8.
Use black, ruff, and mypy.

---

### 🛡 Security Issues

Please do not open GitHub issues for security-related topics.
Report them privately via security guidelines.

---

### 🙌 How to Contribute

1. Fork the repository.
1. Create a branch (`git checkout -b feature/your-feature`).
1. Commit your changes (`git commit -am 'Add feature'`).
1. Push to the branch (`git push origin feature/your-feature`).
1. Create a Pull Request.

---

<!-- END LiminalCognition LLC CONTRIBUTING.MD BLOCK -->


# Contributing to Zircon

If you would like to contribute code you can do so through GitHub by forking the repository and sending a pull request.
When submitting code, please make every effort to follow existing conventions and style in order to keep the code as readable as possible.

## Code
- Zircon is written in Kotlin but you can add your contribution using *Java*
- If you contribute *Java* code put it into `src/main/java`. If you kontribute Kotlin code it should go into `src/main/kotlin`
- If you write implementation code for something put it into the `org.hexworks.zircon.internal` package
  Conversely interfaces and code which expresses an external api should go to the `org.hexworks.zircon.api` package
- If you add implementation code try to follow [the design philosophy behind Zircon](https://github.com/Hexworks/zircon/wiki/The-design-philosophy-behind-Zircon)
- Make sure that you add unit tests for your code and
- Check whether the build passes when creating a pull request

## Submitting a PR
- For every PR there should be an accompanying issue which the PR solves
- The PR itself should only contain code which is the solution for the given issue
- If you are a first time contributor check if there is a [suitable issue](https://github.com/Hexworks/zircon/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) for you

## License

By contributing your code, you agree to license your contribution under the terms of the [MIT](https://github.com/Hexworks/zircon/blob/master/LICENSE) license.
All files are released with the MIT license.
