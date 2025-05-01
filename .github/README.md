<!-- BEGIN LiminalCognition LLC README.MD V0.0.1 BLOCK -->
<a id="readme-top"></a>

<div align="center">

# Coder Plugin

[![Stars](https://img.shields.io/github/stars/RampantLions/coder_plugin?style=social)](https://github.com/RampantLions/coder_plugin/stargazers) &middot; 
[![Fork](https://img.shields.io/github/forks/RampantLions/coder_plugin?style=social)](https://github.com/RampantLions/coder_plugin/network/members) &middot; 
[![Watchers](https://img.shields.io/github/watchers/RampantLions/coder_plugin?style=social)](https://github.com/RampantLions/coder_plugin/watchers) &middot; 
[![Wiki Pages](https://img.shields.io/badge/AREG%20Wiki%20Pages-8-brightgreen?style=social&logo=wikipedia)](https://github.com/RampantLions/coder_plugin/wiki/)
<br />
[![Latest release](https://img.shields.io/github/v/release/RampantLions/coder_plugin?label=Latest%20release&style=social)](https://github.com/RampantLions/coder_plugin/releases/tag/v1.5.0) &middot; 
[![GitHub commits](https://img.shields.io/github/commits-since/RampantLions/coder_plugin/v1.5.0.svg?style=social)](https://GitHub.com/RampantLions/coder_plugin/commit/)
<br/>

[![File A Bug](https://img.shields.io/badge/File%20A%20Bug-blue)](https://github.com/RampantLions/coder_plugin/issues/new?labels=bug)
&middot;

[![Request Enhancement](https://img.shields.io/badge/Request%20Enhancement-blue)](https://github.com/RampantLions/coder_plugin/issues/new?labels=enhancement&template=enhancement.yml)
<br/>

[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black] &middot; 
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)][codecov] &middot; 
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
</div>

# 📋 Read Me

ReadMe is UNDER CONSTRUCTION. 

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">🗂️ About The Project</a>
      <ul>
        <li><a href="#features">📦 Key Features</a></li>
        <li><a href="#built-with">🛠️ Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">🚀 Getting Started</a>
      <ul>
        <li><a href="#quick-start">⚡️ Quick Start</a></li>
        <li><a href="#prerequisites">📋 Prerequisites</a></li>
        <li><a href="#installation">📦 Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">🖥️ Usage</a></li>
    <li><a href="#roadmap">🛣️ Roadmap</a></li>
    <li>
      <a href="#contributing">🤝 Contributing</a>
      <ul>
        <li><a href="#top-contributors">🏆 Top contributors</a></li>
      </ul>
    </li>
    <li><a href="#license">📄 License</a></li>
    <li><a href="#contact">📬 Contact</a></li>
    <li><a href="#acknowledgments">🙏 Acknowledgments</a></li>
  </ol>
</details>

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

<!-- ABOUT THE PROJECT -->
<a id="about-the-project"></a>
## 🗂 About The Project

A plugin system for Python projects using [PDM](https://pdm-project.org/), [uv](https://github.com/astral-sh/uv), and strict development tooling.

Designed for fast setup, strong code quality, and full lifecycle management, from development to publishing.

<br />
<br />
<a href="https://rampantlions.github.io/coder_plugin/"><strong>Explore the docs »</strong></a>
<br />

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

<a id="features"></a>
### 🎯 Key Features

- **PDM-based project management**
- **uv** for fast and reliable installations
- **Strict Python 3.11+ typing** enforced with **mypy**
- **Comprehensive linting** with **ruff**, **black**, and **isort**
- **Coverage reporting** with **pytest-cov**
- **Automated quality checks** via **pre-commit hooks**
- **Fully structured plugin entry points** (scaffolded)
- **Ready for PyPI publishing** with **twine** and **build**

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

<a id="built-with"></a>
### 🛠️ Built With

[black]: https://img.shields.io/badge/black-000000?style=for-the-badge&logo=python&logoColor=white
[black-url]: https://github.com/psf/black

| Tool                                                                                                                                                  | Purpose                                                                                                                                                      |
|:------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![black]][black-url]                                                                                                                                 | Code formatting                                                                                                                                              |
| [![build]][build-url]                                                                                                                                 | Building project distributions (wheel and sdist)                                                                                                             |
| [![cruft]][cruft-url]                                                                                                                                 | Managing and applying updates to projects created from Cookiecutter templates                                                                                |
| [![isort]][isort-url]                                                                                                                                 | Import sorter to automatically organize imports                                                                                                              |
| [![mypy]][mypy-url]                                                                                                                                   | Static type checking for Python                                                                                                                              |
| [![pre-commit]][pre-commit-url]                                                                                                                       | Git hook automation for linting, formatting, and checks                                                                                                      |
| [![pytest]][pytest-url]                                                                                                                               | Unit testing framework                                                                                                                                       |
| [![pytest-cov]][pytest-cov-url]                                                                                                                       | Coverage reporting plugin for pytest                                                                                                                         |
| [![ruff]][ruff-url]                                                                                                                                   | Extremely fast Python linter                                                                                                                                 |
| [![safety]][safety-url]                                                                                                                               | Security vulnerability checker for dependencies                                                                                                              |
| [![semantic-release]][semantic-release-url]                                                                                                           | Automates versioning and changelog generation based on commit messages                                                                                       |
| [![twine]][twine-url]                                                                                                                                 | Securely uploads Python distributions to PyPI                                                                                                                |
| [![Docker Hub]][Docker-Hub-url]                                                                                                                       | Repository for container images (Docker registries)                                                                                                          |
| [![GitHub Actions]][GitHub-Actions-url]                                                                                                               | CI/CD automation platform integrated into GitHub                                                                                                             |
| [![GitHub CLI]][GitHub-CLI-url]                                                                                                                       | Command-line interface to GitHub                                                                                                                             |
| [![GitHub Pages]][GitHub-Pages-url]                                                                                                                   | Hosting service for static websites from GitHub repositories                                                                                                 |
| [![PyPI]][PyPI-url]                                                                                                                                   | [![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)][pypi status] Python Package Index for publishing and distributing Python packages |
| [![MkDocs]][MkDocs-url]                                                                                                                               | Static site generator geared toward project documentation                                                                                                    |
| [![mkdocs-material]][mkdocs-material-url]                                                                                                             | Material Design theme for MkDocs                                                                                                                             |
| [![pipx]][pipx-url]                                                                                                                                   | Tool for installing and running Python applications in isolated environments                                                                                 |

<p align="right"><a href="#readme-top">↖ Back to top</a></p>


[![Status](https://img.shields.io/pypi/status/{{cookiecutter.project_name}}.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}})][pypi status]
[![License](https://img.shields.io/pypi/l/{{cookiecutter.project_name}})][license]

[![Read the documentation at https://{{cookiecutter.project_name}}.readthedocs.io/](https://img.shields.io/readthedocs/{{cookiecutter.project_name}}/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/Tests/badge.svg)][tests]

[pypi status]: https://pypi.org/project/{{cookiecutter.project_name}}/
[read the docs]: https://{{cookiecutter.project_name}}.readthedocs.io/
[tests]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

---

<!-- GETTING STARTED -->
<a id="getting-started"></a>
## 🚀 Getting Started

<a id="quick-start"></a>
### ⚡️ Quick Start

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Abblix OIDC Server library more robust and user-friendly.


<a id="prerequisites"></a>
### 📋 Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

<a id="installation"></a>
### 📦📖 Installation

You can install _{{cookiecutter.friendly_name}}_ via [pip] from [PyPI]:

```console
$ pip install {{cookiecutter.project_name}}
```

1. Install [PDM](https://pdm-project.org/) & [uv](https://github.com/astral-sh/uv):

    ```bash
    brew install pdm uv
    ```

2. Clone the repo
   ```sh
   git clone https://github.com/RampantLions/coder_plugin.git
   ```

2. Change to the cloned repo directory
   ```sh
   cd coder_plugin
   ```

4. Install dependencies:

    ```bash
    pdm install
    ```

3. (Optional) Install pre-commit hooks:

    ```bash
    pdm run pre-commit install
    ```

---

## ⚙️ Development Workflow

- 🧪 **Run tests**:

    ```bash
    pdm run test
    ```

- 🧪 **Run tests with coverage**:

    ```bash
    pdm run test-cov
    ```

- 🧹 **Lint code**:

    ```bash
    pdm run lint
    ```

- 🧹 **Autoformat imports and code**:

    ```bash
    pdm run format
    ```

- 🏗️ **Build project**:

    ```bash
    pdm run build
    ```

- 🌐 **Publish to PyPI**:

    ```bash
    pdm run publish
    ```


<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---

<!-- USAGE EXAMPLES -->
<a id="usage"></a>
## 🖥️ Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---

<!-- ROADMAP -->
<a id="roadmap"></a>
## 🛣️ Roadmap

- [x] Add Item 1
- [x] Add Item 2
- [ ] Add Item 3
- [ ] Add Item 4
- [ ] Add Item 5
    - [ ] Add Item A
    - [ ] Add Item B

See the [open issues](https://github.com/RampantLions/coder_plugin/issues) for a full list of proposed features (and known issues).

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---

<!-- CONTRIBUTING -->
<a id="contributing"></a>
## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to get involved.

Contributions are very welcome.
To learn more, see the [Contributor Guide].

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


The majority of Amplication code is open-source. We are committed to a transparent development process and highly appreciate any contributions. Whether you are helping us fix bugs, proposing new features, improving our documentation or spreading the word - we would love to have you as a part of the Amplication community. Please refer to our contribution guidelines and code of conduct.

* Bug Report: If you see an error message or encounter an issue while using Amplication, please create a bug report.

* Feature Request: If you have an idea or if there is a capability that is missing and would make development easier and more robust, please submit a feature request.

* Documentation Request: If you're reading the Amplication docs and feel like you're missing something, please submit a documentation request.


🤝 Feedback and Contributions

We've made every effort to implement all the main aspects of the OpenID protocol in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Abblix OIDC Server library more robust and user-friendly.

Please feel free to contribute by [submitting an issue](https://github.com/Abblix/Oidc.Server/issues) or [joining the discussions](https://github.com/orgs/Abblix/discussions). Each contribution helps us grow and improve.

We appreciate your support and look forward to making our product even better with your help!


Contributions are very welcome.
To learn more, see the [Contributor Guide].

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


The majority of Amplication code is open-source. We are committed to a transparent development process and highly appreciate any contributions. Whether you are helping us fix bugs, proposing new features, improving our documentation or spreading the word - we would love to have you as a part of the Amplication community. Please refer to our contribution guidelines and code of conduct.

* Bug Report: If you see an error message or encounter an issue while using Amplication, please create a bug report.

* Feature Request: If you have an idea or if there is a capability that is missing and would make development easier and more robust, please submit a feature request.

* Documentation Request: If you're reading the Amplication docs and feel like you're missing something, please submit a documentation request.


🤝 Feedback and Contributions

We've made every effort to implement all the main aspects of the OpenID protocol in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Abblix OIDC Server library more robust and user-friendly.

Please feel free to contribute by [submitting an issue](https://github.com/Abblix/Oidc.Server/issues) or [joining the discussions](https://github.com/orgs/Abblix/discussions). Each contribution helps us grow and improve.

We appreciate your support and look forward to making our product even better with your help!


<a id="top-contributors"></a>
### 🏆 Top contributors:

<a href="https://github.com/RampantLions/coder_plugin/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=RampantLions/coder_plugin" alt="contrib.rocks image" />
</a>

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---

<!-- LICENSE -->
<a id="license"></a>
## 📄 License

This project is licensed under the terms described in the [LICENSE](./LICENSE) file.

A large part of this project is licensed under the Apache 2.0 license. The only exception are the components under the ee (enterprise edition) directory, these are licensed under the Amplication Enterprise Edition license.

Distributed under the terms of the [{{cookiecutter.license.replace("-", " ")}} license][./LICENSE],
_{{cookiecutter.friendly_name}}_ is free and open source software.

[license]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/.github/LICENSE

<p align="right"><a href="#readme-top">↖ Back to top</a></p>
---

<!-- CONTACT -->
<a id="contact"></a>
## 📬 Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


🗨️ Contacts

For more details about our products, services, or any general information regarding the Abblix OIDC Server, feel free to reach out to us. We are here to provide support and answer any questions you may have. Below are the best ways to contact our team:

- **Email**: Send us your inquiries or support requests at [support@abblix.com](mailto:support@abblix.com).
- **Website**: Visit the official Abblix OIDC Server page for more information: [Abblix OIDC Server](https://www.abblix.com/abblix-oidc-server).

Subscribe to our LinkedIn and Twitter:


We look forward to assisting you and ensuring your experience with our products is successful and enjoyable!

[Back to top](#top)


<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---

<!-- RESOURCES -->
<a id="resources"></a>
## 📚 Resources

<details open>
<summary>
Running Amplication
</summary> <br />

> **Note**
> It is also possible to start development with GitHub Codespaces, when navigating to `< > Code`, select `Codespaces` instead of `Local`. Click on either the `+`-sign or the `Create codespace on master`-button.

Amplication is using a monorepo architecture - powered by <a href="https://nx.dev">Nx Workspaces</a> - where multiple applications and libraries exist in a single repository. To setup a local development environment the following steps can be followed:
</details>


> [!NOTE]
> AREG currently supports **Local** (multithreading) and **Public** (multiprocessing) services.

> [!IMPORTANT]
> The binds system has changed. Instead of doing the name of the key, there are scancodes assigned per key.


> :warning: **Attention:** switch to the desired Scala version (**2.12** or **2.13**) when using the links or JARs names.

> :memo: **Note:** as seen on [Spark docs](https://spark.apache.org/docs/latest/configuration.html#dynamically-loading-spark-properties), properties set programmatically on the Spark Context take highest precedence, then flags passed through CLI calls like `spark-submit` or `spark-shell`, then options in the `spark-defaults.conf` file.

> :memo: **Notes:**
> - While the `/proc/meminfo` file shows kilobytes (kB; 1 kB equals 1000 B), its unit is actually kibibytes (KiB; 1 KiB equals 1024 B). This imprecision is known, but is not corrected due to legacy concerns.
> - Many fields have been present since at least Linux 2.6.0, but most of the other fields are available at specific Linux versions (as noted in each method docstring) or are displayed only if the kernel was configured with specific options. If these fields are not found, the metrics won't be registered onto Dropwizard's metric system.


> This, milord, is my family's axe. We have owned it for almost nine hundred years, see. Of course,
sometimes it needed a new blade. And sometimes it has required a new handle, new designs on the
metalwork, a little refreshing of the ornamentation ... but is this not the nine hundred-year-old
axe of my family? And because it has changed gently over time, it is still a pretty good axe,
y'know. Pretty good.

> -- Terry Pratchett, The Fifth Elephant <br>
> &nbsp;&nbsp;&nbsp; reflecting on identity, flow and derived values  (aka [The Ship of Theseus](https://en.wikipedia.org/wiki/Ship_of_Theseus))
<br/>
<br/>

---

<!-- ACKNOWLEDGMENTS -->
<a id="acknowledgments"></a>
## 🙏 Acknowledgments


* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RampantLions/coder_plugin.svg?style=for-the-badge
[contributors-url]: https://github.com/RampantLions/coder_plugin/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/RampantLions/coder_plugin.svg?style=for-the-badge
[forks-url]: https://github.com/RampantLions/coder_plugin/network/members
[stars-shield]: https://img.shields.io/github/stars/RampantLions/coder_plugin.svg?style=for-the-badge
[stars-url]: https://github.com/RampantLions/coder_plugin/stargazers
[issues-shield]: https://img.shields.io/github/issues/RampantLions/coder_plugin.svg?style=for-the-badge
[issues-url]: https://github.com/RampantLions/coder_plugin/issues
[license-shield]: https://img.shields.io/github/license/RampantLions/coder_plugin.svg?style=for-the-badge
[license-url]: https://github.com/RampantLions/coder_plugin/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/wiechman
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[build]: https://img.shields.io/badge/build-3670A0?style=for-the-badge&logo=python&logoColor=white
[build-url]: https://pypi.org/project/build/
[cruft]: https://img.shields.io/badge/cruft-563D7C?style=for-the-badge&logo=python&logoColor=white
[cruft-url]: https://github.com/cruft/cruft
[isort]: https://img.shields.io/badge/isort-0B0B0B?style=for-the-badge&logo=python&logoColor=white
[isort-url]: https://pycqa.github.io/isort/
[mypy]: https://img.shields.io/badge/mypy-3776AB?style=for-the-badge&logo=python&logoColor=white
[mypy-url]: https://github.com/python/mypy
[pre-commit]: https://img.shields.io/badge/pre--commit-F7B93E?style=for-the-badge&logo=pre-commit&logoColor=black
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[pytest]: https://img.shields.io/badge/pytest-0A0A0A?style=for-the-badge&logo=pytest&logoColor=white
[pytest-url]: https://docs.pytest.org/en/latest/
[pytest-cov]: https://img.shields.io/badge/pytest--cov-0A0A0A?style=for-the-badge&logo=pytest&logoColor=white
[pytest-cov-url]: https://pytest-cov.readthedocs.io/en/latest/
[ruff]: https://img.shields.io/badge/ruff-0B0B0B?style=for-the-badge&logo=python&logoColor=white
[ruff-url]: https://github.com/astral/ruff
[safety]: https://img.shields.io/badge/safety-FF4B4B?style=for-the-badge&logo=python&logoColor=white
[safety-url]: https://pyup.io/safety/
[semantic-release]: https://img.shields.io/badge/semantic--release-4945FF?style=for-the-badge&logo=semantic-release&logoColor=white
[semantic-release-url]: https://github.com/semantic-release/semantic-release
[twine]: https://img.shields.io/badge/twine-3776AB?style=for-the-badge&logo=python&logoColor=white
[twine-url]: https://twine.readthedocs.io/en/latest/
[Docker Hub]: https://img.shields.io/badge/docker--hub-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-Hub-url]: https://hub.docker.com/
[GitHub Actions]: https://img.shields.io/badge/github--actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white
[GitHub-Actions-url]: https://github.com/features/actions
[GitHub CLI]: https://img.shields.io/badge/github--cli-4183C4?style=for-the-badge&logo=github&logoColor=white
[GitHub-CLI-url]: https://cli.github.com/
[GitHub Pages]: https://img.shields.io/badge/github--pages-121013?style=for-the-badge&logo=githubpages&logoColor=white
[GitHub-Pages-url]: https://pages.github.com/
[PyPI]: https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white
[PyPI-url]: https://pypi.org/
[MkDocs]: https://img.shields.io/badge/mkdocs-000000?style=for-the-badge&logo=mkdocs&logoColor=white
[MkDocs-url]: https://github.com/mkdocs/mkdocs
[mkdocs-material]: https://img.shields.io/badge/mkdocs--material-000000?style=for-the-badge&logo=materialdesign&logoColor=white
[mkdocs-material-url]: https://github.com/squidfunk/mkdocs-material
[pipx]: https://img.shields.io/badge/pipx-3776AB?style=for-the-badge&logo=python&logoColor=white
[pipx-url]: https://github.com/pypa/pipx

---

## 🧩 Plugin System (Optional)

The template includes a scaffold for exposing plugins through [Python entry points](https://packaging.python.org/en/latest/specifications/entry-points/).

This allows you to design modular, extensible applications if needed.
Example groups are ready to be customized for your own plugin architecture.

---

## 🛡️ Project Status

This is a stable template intended for production use.
Actively maintained by [RampantLions](https://github.com/RampantLions).

Contributions and feedback are welcome.

---

## ⛓ Useful Links

- 🔗 [Project Homepage](https://RampantLions.github.io/coder_plugin/)
- 🔗 [Source Repository](https://github.com/RampantLions/coder_plugin)
- 🔗 [Issue Tracker](https://github.com/RampantLions/coder_plugin/issues)
- 🔗 [Python Packaging Guide](https://packaging.python.org/)
- 🔗 [PDM Documentation](https://pdm-project.org/)

---

## 🔒 Security & 🛡 Security Issues

For details on reporting vulnerabilities, see [SECURITY.md](./SECURITY.md).



---


🎓 Certification

[![OpenID_Foundation_Certification](https://resources.abblix.com/imgs/svg/abblix-oidc-server-openid-foundation-certification-mark.svg)](https://openid.net/certification/#OPENID-OP-P)

We are certified in all profiles. During the certification process, we skipped ZERO tests and received NO warnings. All **630** tests ![Passed](https://img.shields.io/badge/PASSED-brightgreen). We are extremely proud of this achievement. It reflects our overall approach to any endeavor. For more details, click the links ([Certified OpenID Providers & Profiles](https://openid.net/certification/#OPENID-OP-P), [Certified OpenID Providers for Logout Profiles](https://openid.net/certification/#OPENID-OP-LP)).

For convenience, the certification information is provided in the tables below:

---

Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [dbt Code of Conduct](https://community.getdbt.com/code-of-conduct).

---

Support

<a href="https://buymeacoffee.com/RampantLions" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p>

<a href="https://www.patreon.com/RampantLions">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

---

> GitHub [@RampantLions](https://github.com/RampantLions) &nbsp;&middot;&nbsp;
> Twitter [@RampantLions](https://twitter.com/RampantLions)
> <a href="https://www.linkedin.com/shareArticle?mini=true&url=https%3A//github.com/RampantLions/coder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=LinkedIn&logo=LinkedIn&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on LinkedIn"/></a>

[![LinkedIn](https://img.shields.io/badge/subscribe-white.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTIwLjQ0NyAyMC40NTJoLTMuNTU0di01LjU2OWMwLTEuMzI4LS4wMjctMy4wMzctMS44NTItMy4wMzctMS44NTMgMC0yLjEzNiAxLjQ0NS0yLjEzNiAyLjkzOXY1LjY2N0g5LjM1MVY5aDMuNDE0djEuNTYxaC4wNDZjLjQ3Ny0uOSAxLjYzNy0xLjg1IDMuMzctMS44NSAzLjYwMSAwIDQuMjY3IDIuMzcgNC4yNjcgNS40NTV2Ni4yODZ6TTUuMzM3IDcuNDMzYTIuMDYyIDIuMDYyIDAgMCAxLTIuMDYzLTIuMDY1IDIuMDY0IDIuMDY0IDAgMSAxIDIuMDYzIDIuMDY1em0xLjc4MiAxMy4wMTlIMy41NTVWOWgzLjU2NHYxMS40NTJ6TTIyLjIyNSAwSDEuNzcxQy43OTIgMCAwIC43NzQgMCAxLjcyOXYyMC41NDJDMCAyMy4yMjcuNzkyIDI0IDEuNzcxIDI0aDIwLjQ1MUMyMy4yIDI0IDI0IDIzLjIyNyAyNCAyMi4yNzFWMS43MjlDMjQgLjc3NCAyMy4yIDAgMjIuMjIyIDBoLjAwM3oiIGZpbGw9IiMwQTY2QzIiLz48cGF0aCBzdHlsZT0iZmlsbDojZmZmO3N0cm9rZS13aWR0aDouMDIwOTI0MSIgZD0iTTQuOTE3IDcuMzc3YTIuMDUyIDIuMDUyIDAgMCAxLS4yNC0zLjk0OWMxLjEyNS0uMzg0IDIuMzM5LjI3NCAyLjY1IDEuNDM3LjA2OC4yNS4wNjguNzY3LjAwMSAxLjAxYTIuMDg5IDIuMDg5IDAgMCAxLTEuNjIgMS41MSAyLjMzNCAyLjMzNCAwIDAgMS0uNzktLjAwOHoiLz48cGF0aCBzdHlsZT0iZmlsbDojZmZmO3N0cm9rZS13aWR0aDouMDIwOTI0MSIgZD0iTTQuOTE3IDcuMzc3YTIuMDU2IDIuMDU2IDAgMCAxLTEuNTItMi42NyAyLjA0NyAyLjA0NyAwIDAgMSAzLjQxOS0uNzU2Yy4yNC4yNTQuNDIuNTczLjUxMi45MDguMDY1LjI0LjA2NS43OCAwIDEuMDItLjA1MS4xODYtLjE5Ny41MDQtLjMuNjUyLS4wOS4xMzItLjMxLjM2Mi0uNDQzLjQ2NC0uNDYzLjM1Ny0xLjEuNTAzLTEuNjY4LjM4MlpNMy41NTcgMTQuNzJWOS4wMDhoMy41NTd2MTEuNDI0SDMuNTU3Wk05LjM1MyAxNC43MlY5LjAwOGgzLjQxMXYuNzg1YzAgLjYxNC4wMDUuNzg0LjAyNi43ODMuMDE0IDAgLjA3LS4wNzMuMTI0LS4xNjIuNTI0LS44NjUgMS41MDgtMS40NzggMi42NS0xLjY1LjI3NS0uMDQyIDEtLjA0NyAxLjMzMi0uMDA5Ljc5LjA5IDEuNDUxLjMxNiAxLjk0LjY2NC4yMi4xNTcuNTU3LjQ5My43MTQuNzEzLjQyLjU5Mi42OSAxLjQxMi44MDggMi40NjQuMDc0LjY2My4wODQgMS4yMTUuMDg1IDQuNTc4djMuMjU4aC0zLjUzNnYtMi45ODZjMC0yLjk3LS4wMS0zLjQ3NC0uMDc0LTMuOTA4LS4wOS0uNjA2LS4zMTQtMS4wODItLjYzNC0xLjM0Mi0uMzk1LS4zMjItMS4wMjktLjQzNy0xLjcwMy0uMzA5LS44NTguMTYzLTEuMzU1Ljc1LTEuNTIzIDEuNzk3LS4wNzYuNDcxLS4wODQuODQ1LS4wODQgMy44MzR2Mi45MTRIOS4zNTN6Ii8+PC9zdmc+)](https://www.linkedin.com/company/103540510/)
[![X](https://img.shields.io/badge/subscribe-white.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTE4LjkwMSAxLjE1M2gzLjY4bC04LjA0IDkuMTlMMjQgMjIuODQ2aC03LjQwNmwtNS44LTcuNTg0LTYuNjM4IDcuNTg0SC40NzRsOC42LTkuODNMMCAxLjE1NGg3LjU5NGw1LjI0MyA2LjkzMlpNMTcuNjEgMjAuNjQ0aDIuMDM5TDYuNDg2IDMuMjRINC4yOThaIi8+PHBhdGggc3R5bGU9ImZpbGw6I2ZmZjtzdHJva2Utd2lkdGg6LjAyMDkyNDEiIGQ9Ik0xMS4wMzYgMTIuMDI4IDQuMzg3IDMuMzM0bC0uMDYtLjA4SDYuNDhsNi41MTYgOC42MTQgNi41NzUgOC42OTQuMDYuMDhoLTIuMDA2eiIvPjwvc3ZnPg==)](https://twitter.com/OIDCServer)

<a href="https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin&title=Awesome%20communcation%20engine!" target="_blank"><img src="https://img.shields.io/twitter/url?label=Reddit&logo=Reddit&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on Reddit"/></a>&nbsp;
&nbsp;
<a href="https://x.com/intent/tweet?text=%23AREG%20%23realtime%20communication%20engine%20for%20%23embedded%20and%20%23IoT%0A%0Ahttps%3A//github.com/RampantLions/coder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=Twitter&logo=X&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Shared on X"/></a>&nbsp;
<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/RampantLions/coder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=Facebook&logo=Facebook&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on Facebook"/></a>&nbsp;
<a href="https://t.me/share/url?text=Awesome%20communication%20engine!&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=Telegram&logo=Telegram&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on Telegram"/></a>&nbsp;
<a href="https://wa.me/?text=Awesome%20communication%20engine!%5Cn%20https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=Whatsapp&logo=Whatsapp&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on Whatsapp"/></a>&nbsp;
<a href="mailto:?subject=Awesome%20communication%20engine&body=Checkout%20this%20awesome%20communication%20engine%3A%0Ahttps%3A//github.com/RampantLions/coder_plugin%0A" target="_blank"><img src="https://img.shields.io/twitter/url?label=GMail&logo=GMail&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin"/></a>


<!-- END LiminalCognition LLC README.MD BLOCK -->

📖 


[pypi status]: https://pypi.org/project/{{cookiecutter.project_name}}/


[![Status](https://img.shields.io/pypi/status/{{cookiecutter.project_name}}.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}})][pypi status]
[![License](https://img.shields.io/pypi/l/{{cookiecutter.project_name}})][license]

[![Read the documentation at https://{{cookiecutter.project_name}}.readthedocs.io/](https://img.shields.io/readthedocs/{{cookiecutter.project_name}}/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]

[read the docs]: https://{{cookiecutter.project_name}}.readthedocs.io/
[tests]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Requirements

- TODO

## Installation

You can install _{{cookiecutter.friendly_name}}_ via [pip] from [PyPI]:

```console
$ pip install {{cookiecutter.project_name}}
```

## Usage

Please see the [Command-line Reference] for details.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@RampantLions]'s [Python Cookiecutter] template.

[@RampantLions]: https://github.com/RampantLions
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/RampantLions/cookiecutter-hypermodern-python
[file an issue]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/.github/LICENSE
[contributor guide]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/.github/CONTRIBUTING.md
[command-line reference]: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/usage.html




















---


<!-- GETTING STARTED -->
<a id="getting-started"></a>
## 🚀 Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Abblix OIDC Server library more robust and user-friendly.


<a id="prerequisites"></a>
### 📋 Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

<a id="installation"></a>
### 📦 Installation

1. Install [PDM](https://pdm-project.org/) & [uv](https://github.com/astral-sh/uv):

    ```bash
    brew install pdm uv
    ```

2. Clone the repo
   ```sh
   git clone https://github.com/RampantLions/coder_plugin.git
   ```

2. Change to the cloned repo directory
   ```sh
   cd coder_plugin
   ```

4. Install dependencies:

    ```bash
    pdm install
    ```

3. (Optional) Install pre-commit hooks:

    ```bash
    pdm run pre-commit install
    ```

---

## ⚙️ Development Workflow

- 🧪 **Run tests**:

    ```bash
    pdm run test
    ```

- 🧪 **Run tests with coverage**:

    ```bash
    pdm run test-cov
    ```

- 🧹 **Lint code**:

    ```bash
    pdm run lint
    ```

- 🧹 **Autoformat imports and code**:

    ```bash
    pdm run format
    ```

- 🏗️ **Build project**:

    ```bash
    pdm run build
    ```

- 🌐 **Publish to PyPI**:

    ```bash
    pdm run publish
    ```


<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---

<!-- USAGE EXAMPLES -->
<a id="usage"></a>
## 🖥️ Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---



---



<a id="top-contributors"></a>
### 🏆 Top contributors:

<a href="https://github.com/RampantLions/coder_plugin/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=RampantLions/coder_plugin" alt="contrib.rocks image" />
</a>

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---

<!-- LICENSE -->
<a id="license"></a>
## 📄 License

This project is licensed under the terms described in the [LICENSE](./LICENSE) file.

A large part of this project is licensed under the Apache 2.0 license. The only exception are the components under the ee (enterprise edition) directory, these are licensed under the Amplication Enterprise Edition license.

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

Distributed under the terms of the [{{cookiecutter.license.replace("-", " ")}} license][./LICENSE],
_{{cookiecutter.friendly_name}}_ is free and open source software.

---

<!-- CONTACT -->
<a id="contact"></a>
## 📬 Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


🗨️ Contacts

For more details about our products, services, or any general information regarding the Abblix OIDC Server, feel free to reach out to us. We are here to provide support and answer any questions you may have. Below are the best ways to contact our team:

- **Email**: Send us your inquiries or support requests at [support@abblix.com](mailto:support@abblix.com).
- **Website**: Visit the official Abblix OIDC Server page for more information: [Abblix OIDC Server](https://www.abblix.com/abblix-oidc-server).

Subscribe to our LinkedIn and Twitter:

[![LinkedIn](https://img.shields.io/badge/subscribe-white.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTIwLjQ0NyAyMC40NTJoLTMuNTU0di01LjU2OWMwLTEuMzI4LS4wMjctMy4wMzctMS44NTItMy4wMzctMS44NTMgMC0yLjEzNiAxLjQ0NS0yLjEzNiAyLjkzOXY1LjY2N0g5LjM1MVY5aDMuNDE0djEuNTYxaC4wNDZjLjQ3Ny0uOSAxLjYzNy0xLjg1IDMuMzctMS44NSAzLjYwMSAwIDQuMjY3IDIuMzcgNC4yNjcgNS40NTV2Ni4yODZ6TTUuMzM3IDcuNDMzYTIuMDYyIDIuMDYyIDAgMCAxLTIuMDYzLTIuMDY1IDIuMDY0IDIuMDY0IDAgMSAxIDIuMDYzIDIuMDY1em0xLjc4MiAxMy4wMTlIMy41NTVWOWgzLjU2NHYxMS40NTJ6TTIyLjIyNSAwSDEuNzcxQy43OTIgMCAwIC43NzQgMCAxLjcyOXYyMC41NDJDMCAyMy4yMjcuNzkyIDI0IDEuNzcxIDI0aDIwLjQ1MUMyMy4yIDI0IDI0IDIzLjIyNyAyNCAyMi4yNzFWMS43MjlDMjQgLjc3NCAyMy4yIDAgMjIuMjIyIDBoLjAwM3oiIGZpbGw9IiMwQTY2QzIiLz48cGF0aCBzdHlsZT0iZmlsbDojZmZmO3N0cm9rZS13aWR0aDouMDIwOTI0MSIgZD0iTTQuOTE3IDcuMzc3YTIuMDUyIDIuMDUyIDAgMCAxLS4yNC0zLjk0OWMxLjEyNS0uMzg0IDIuMzM5LjI3NCAyLjY1IDEuNDM3LjA2OC4yNS4wNjguNzY3LjAwMSAxLjAxYTIuMDg5IDIuMDg5IDAgMCAxLTEuNjIgMS41MSAyLjMzNCAyLjMzNCAwIDAgMS0uNzktLjAwOHoiLz48cGF0aCBzdHlsZT0iZmlsbDojZmZmO3N0cm9rZS13aWR0aDouMDIwOTI0MSIgZD0iTTQuOTE3IDcuMzc3YTIuMDU2IDIuMDU2IDAgMCAxLTEuNTItMi42NyAyLjA0NyAyLjA0NyAwIDAgMSAzLjQxOS0uNzU2Yy4yNC4yNTQuNDIuNTczLjUxMi45MDguMDY1LjI0LjA2NS43OCAwIDEuMDItLjA1MS4xODYtLjE5Ny41MDQtLjMuNjUyLS4wOS4xMzItLjMxLjM2Mi0uNDQzLjQ2NC0uNDYzLjM1Ny0xLjEuNTAzLTEuNjY4LjM4MlpNMy41NTcgMTQuNzJWOS4wMDhoMy41NTd2MTEuNDI0SDMuNTU3Wk05LjM1MyAxNC43MlY5LjAwOGgzLjQxMXYuNzg1YzAgLjYxNC4wMDUuNzg0LjAyNi43ODMuMDE0IDAgLjA3LS4wNzMuMTI0LS4xNjIuNTI0LS44NjUgMS41MDgtMS40NzggMi42NS0xLjY1LjI3NS0uMDQyIDEtLjA0NyAxLjMzMi0uMDA5Ljc5LjA5IDEuNDUxLjMxNiAxLjk0LjY2NC4yMi4xNTcuNTU3LjQ5My43MTQuNzEzLjQyLjU5Mi42OSAxLjQxMi44MDggMi40NjQuMDc0LjY2My4wODQgMS4yMTUuMDg1IDQuNTc4djMuMjU4aC0zLjUzNnYtMi45ODZjMC0yLjk3LS4wMS0zLjQ3NC0uMDc0LTMuOTA4LS4wOS0uNjA2LS4zMTQtMS4wODItLjYzNC0xLjM0Mi0uMzk1LS4zMjItMS4wMjktLjQzNy0xLjcwMy0uMzA5LS44NTguMTYzLTEuMzU1Ljc1LTEuNTIzIDEuNzk3LS4wNzYuNDcxLS4wODQuODQ1LS4wODQgMy44MzR2Mi45MTRIOS4zNTN6Ii8+PC9zdmc+)](https://www.linkedin.com/company/103540510/)
[![X](https://img.shields.io/badge/subscribe-white.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTE4LjkwMSAxLjE1M2gzLjY4bC04LjA0IDkuMTlMMjQgMjIuODQ2aC03LjQwNmwtNS44LTcuNTg0LTYuNjM4IDcuNTg0SC40NzRsOC42LTkuODNMMCAxLjE1NGg3LjU5NGw1LjI0MyA2LjkzMlpNMTcuNjEgMjAuNjQ0aDIuMDM5TDYuNDg2IDMuMjRINC4yOThaIi8+PHBhdGggc3R5bGU9ImZpbGw6I2ZmZjtzdHJva2Utd2lkdGg6LjAyMDkyNDEiIGQ9Ik0xMS4wMzYgMTIuMDI4IDQuMzg3IDMuMzM0bC0uMDYtLjA4SDYuNDhsNi41MTYgOC42MTQgNi41NzUgOC42OTQuMDYuMDhoLTIuMDA2eiIvPjwvc3ZnPg==)](https://twitter.com/OIDCServer)

We look forward to assisting you and ensuring your experience with our products is successful and enjoyable!

[Back to top](#top)


<p align="right"><a href="#readme-top">↖ Back to top</a></p>

---

<!-- RESOURCES -->
<a id="resources"></a>
## 📚 Resources

<details open>
<summary>
Running Amplication
</summary> <br />

> **Note**
> It is also possible to start development with GitHub Codespaces, when navigating to `< > Code`, select `Codespaces` instead of `Local`. Click on either the `+`-sign or the `Create codespace on master`-button.

Amplication is using a monorepo architecture - powered by <a href="https://nx.dev">Nx Workspaces</a> - where multiple applications and libraries exist in a single repository. To setup a local development environment the following steps can be followed:
</details>


> [!NOTE]
> AREG currently supports **Local** (multithreading) and **Public** (multiprocessing) services.

> [!IMPORTANT]
> The binds system has changed. Instead of doing the name of the key, there are scancodes assigned per key.


> :warning: **Attention:** switch to the desired Scala version (**2.12** or **2.13**) when using the links or JARs names.

> :memo: **Note:** as seen on [Spark docs](https://spark.apache.org/docs/latest/configuration.html#dynamically-loading-spark-properties), properties set programmatically on the Spark Context take highest precedence, then flags passed through CLI calls like `spark-submit` or `spark-shell`, then options in the `spark-defaults.conf` file.

> :memo: **Notes:**
> - While the `/proc/meminfo` file shows kilobytes (kB; 1 kB equals 1000 B), its unit is actually kibibytes (KiB; 1 KiB equals 1024 B). This imprecision is known, but is not corrected due to legacy concerns.
> - Many fields have been present since at least Linux 2.6.0, but most of the other fields are available at specific Linux versions (as noted in each method docstring) or are displayed only if the kernel was configured with specific options. If these fields are not found, the metrics won't be registered onto Dropwizard's metric system.


> This, milord, is my family's axe. We have owned it for almost nine hundred years, see. Of course,
sometimes it needed a new blade. And sometimes it has required a new handle, new designs on the
metalwork, a little refreshing of the ornamentation ... but is this not the nine hundred-year-old
axe of my family? And because it has changed gently over time, it is still a pretty good axe,
y'know. Pretty good.

> -- Terry Pratchett, The Fifth Elephant <br>
> &nbsp;&nbsp;&nbsp; reflecting on identity, flow and derived values  (aka [The Ship of Theseus](https://en.wikipedia.org/wiki/Ship_of_Theseus))
<br/>
<br/>

---

<!-- ACKNOWLEDGMENTS -->
<a id="acknowledgments"></a>
## 🙏 Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right"><a href="#readme-top">↖ Back to top</a></p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RampantLions/coder_plugin.svg?style=for-the-badge
[contributors-url]: https://github.com/RampantLions/coder_plugin/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/RampantLions/coder_plugin.svg?style=for-the-badge
[forks-url]: https://github.com/RampantLions/coder_plugin/network/members
[stars-shield]: https://img.shields.io/github/stars/RampantLions/coder_plugin.svg?style=for-the-badge
[stars-url]: https://github.com/RampantLions/coder_plugin/stargazers
[issues-shield]: https://img.shields.io/github/issues/RampantLions/coder_plugin.svg?style=for-the-badge
[issues-url]: https://github.com/RampantLions/coder_plugin/issues
[license-shield]: https://img.shields.io/github/license/RampantLions/coder_plugin.svg?style=for-the-badge
[license-url]: https://github.com/RampantLions/coder_plugin/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/wiechman
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[black]: https://img.shields.io/badge/black-000000?style=for-the-badge&logo=python&logoColor=white
[black-url]: https://github.com/psf/black
[build]: https://img.shields.io/badge/build-3670A0?style=for-the-badge&logo=python&logoColor=white
[build-url]: https://pypi.org/project/build/
[cruft]: https://img.shields.io/badge/cruft-563D7C?style=for-the-badge&logo=python&logoColor=white
[cruft-url]: https://github.com/cruft/cruft
[isort]: https://img.shields.io/badge/isort-0B0B0B?style=for-the-badge&logo=python&logoColor=white
[isort-url]: https://pycqa.github.io/isort/
[mypy]: https://img.shields.io/badge/mypy-3776AB?style=for-the-badge&logo=python&logoColor=white
[mypy-url]: https://github.com/python/mypy
[pre-commit]: https://img.shields.io/badge/pre--commit-F7B93E?style=for-the-badge&logo=pre-commit&logoColor=black
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[pytest]: https://img.shields.io/badge/pytest-0A0A0A?style=for-the-badge&logo=pytest&logoColor=white
[pytest-url]: https://docs.pytest.org/en/latest/
[pytest-cov]: https://img.shields.io/badge/pytest--cov-0A0A0A?style=for-the-badge&logo=pytest&logoColor=white
[pytest-cov-url]: https://pytest-cov.readthedocs.io/en/latest/
[ruff]: https://img.shields.io/badge/ruff-0B0B0B?style=for-the-badge&logo=python&logoColor=white
[ruff-url]: https://github.com/astral/ruff
[safety]: https://img.shields.io/badge/safety-FF4B4B?style=for-the-badge&logo=python&logoColor=white
[safety-url]: https://pyup.io/safety/
[semantic-release]: https://img.shields.io/badge/semantic--release-4945FF?style=for-the-badge&logo=semantic-release&logoColor=white
[semantic-release-url]: https://github.com/semantic-release/semantic-release
[twine]: https://img.shields.io/badge/twine-3776AB?style=for-the-badge&logo=python&logoColor=white
[twine-url]: https://twine.readthedocs.io/en/latest/
[Docker Hub]: https://img.shields.io/badge/docker--hub-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-Hub-url]: https://hub.docker.com/
[GitHub Actions]: https://img.shields.io/badge/github--actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white
[GitHub-Actions-url]: https://github.com/features/actions
[GitHub CLI]: https://img.shields.io/badge/github--cli-4183C4?style=for-the-badge&logo=github&logoColor=white
[GitHub-CLI-url]: https://cli.github.com/
[GitHub Pages]: https://img.shields.io/badge/github--pages-121013?style=for-the-badge&logo=githubpages&logoColor=white
[GitHub-Pages-url]: https://pages.github.com/
[PyPI]: https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white
[PyPI-url]: https://pypi.org/
[MkDocs]: https://img.shields.io/badge/mkdocs-000000?style=for-the-badge&logo=mkdocs&logoColor=white
[MkDocs-url]: https://github.com/mkdocs/mkdocs
[mkdocs-material]: https://img.shields.io/badge/mkdocs--material-000000?style=for-the-badge&logo=materialdesign&logoColor=white
[mkdocs-material-url]: https://github.com/squidfunk/mkdocs-material
[pipx]: https://img.shields.io/badge/pipx-3776AB?style=for-the-badge&logo=python&logoColor=white
[pipx-url]: https://github.com/pypa/pipx

---

## 🧩 Plugin System (Optional)

The template includes a scaffold for exposing plugins through [Python entry points](https://packaging.python.org/en/latest/specifications/entry-points/).

This allows you to design modular, extensible applications if needed.
Example groups are ready to be customized for your own plugin architecture.

---


## 🎓 Certification

[![OpenID_Foundation_Certification](https://resources.abblix.com/imgs/svg/abblix-oidc-server-openid-foundation-certification-mark.svg)](https://openid.net/certification/#OPENID-OP-P)

We are certified in all profiles. During the certification process, we skipped ZERO tests and received NO warnings. All **630** tests ![Passed](https://img.shields.io/badge/PASSED-brightgreen). We are extremely proud of this achievement. It reflects our overall approach to any endeavor. For more details, click the links ([Certified OpenID Providers & Profiles](https://openid.net/certification/#OPENID-OP-P), [Certified OpenID Providers for Logout Profiles](https://openid.net/certification/#OPENID-OP-LP)).

For convenience, the certification information is provided in the tables below:

---

Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [dbt Code of Conduct](https://community.getdbt.com/code-of-conduct).

---

Support

<a href="https://buymeacoffee.com/RampantLions" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p>

<a href="https://www.patreon.com/RampantLions">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

---

## Usage

Please see the [Command-line Reference] for details.

## Credits

This project was generated from [@RampantLions]'s [Python Cookiecutter] template.

> GitHub [@RampantLions](https://github.com/RampantLions) &nbsp;&middot;&nbsp;
> Twitter [@RampantLions](https://twitter.com/RampantLions)


<a href="https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin&title=Awesome%20communcation%20engine!" target="_blank"><img src="https://img.shields.io/twitter/url?label=Reddit&logo=Reddit&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on Reddit"/></a>&nbsp;
<a href="https://www.linkedin.com/shareArticle?mini=true&url=https%3A//github.com/RampantLions/coder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=LinkedIn&logo=LinkedIn&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on LinkedIn"/></a>&nbsp;
<a href="https://x.com/intent/tweet?text=%23AREG%20%23realtime%20communication%20engine%20for%20%23embedded%20and%20%23IoT%0A%0Ahttps%3A//github.com/RampantLions/coder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=Twitter&logo=X&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Shared on X"/></a>&nbsp;
<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/RampantLions/coder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=Facebook&logo=Facebook&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on Facebook"/></a>&nbsp;
<a href="https://t.me/share/url?text=Awesome%20communication%20engine!&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=Telegram&logo=Telegram&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on Telegram"/></a>&nbsp;
<a href="https://wa.me/?text=Awesome%20communication%20engine!%5Cn%20https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" target="_blank"><img src="https://img.shields.io/twitter/url?label=Whatsapp&logo=Whatsapp&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin" alt="Share on Whatsapp"/></a>&nbsp;
<a href="mailto:?subject=Awesome%20communication%20engine&body=Checkout%20this%20awesome%20communication%20engine%3A%0Ahttps%3A//github.com/RampantLions/coder_plugin%0A" target="_blank"><img src="https://img.shields.io/twitter/url?label=GMail&logo=GMail&style=social&url=https%3A%2F%2Fgithub.com%2FRampantLions%2Fcoder_plugin"/></a>


<!-- END LiminalCognition LLC README.MD BLOCK -->





## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.





[@RampantLions]: https://github.com/RampantLions
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/RampantLions/cookiecutter-hypermodern-python
[file an issue]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[contributor guide]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/.github/CONTRIBUTING.md
[command-line reference]: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/usage.html
