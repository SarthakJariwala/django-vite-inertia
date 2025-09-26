# Django with Vite and Inertia 🚀

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)

A modern template for supercharging your Django project with [Vite](https://vitejs.dev/) for lightning-fast frontend builds and [Inertia](https://inertiajs.com/) for seamless SPA-like experiences without the API complexity.

![Demo](./demo.gif)

## ✨ Features

- **Multiple Frontend Options**

  - Vue
  - React (with optional shadcn/ui components)
  - Svelte

- **Styling Options**

  - Tailwind CSS (optional)
  - Custom CSS

- **Database Options**

  - PostgreSQL
  - SQLite (configured for production if selected)

- **Authentication Options**

  - django-allauth (optional)

- **Development & Deployment**
  - Docker support (optional)
    - Development environment
    - Production-ready setup

## 🚦 Getting Started

### Using [uv](https://docs.astral.sh/uv/) (Recommended)

```bash
mkdir myproject
uvx copier copy gh:sarthakjariwala/django-vite-inertia myproject
```

### Using [pipx](https://pipx.pypa.io/stable/)

```bash
mkdir myproject
pipx run copier copy gh:sarthakjariwala/django-vite-inertia myproject
```

### Using [copier](https://copier.readthedocs.io/en/stable/)

```bash
mkdir awesome-project
copier copy gh:sarthakjariwala/django-vite-inertia awesome-project
```

## 🔄 Updating Your Project

Keep your project up-to-date with the latest template changes:

```bash
cd awesome-project
uvx copier update
# OR
copier update
```

## 📜 License

MIT License

## 🙏 Acknowledgements

Standing on the shoulders of giants:

- [Django](https://www.djangoproject.com/)
- [Vite](https://vitejs.dev/)
- [Inertia](https://inertiajs.com/)
- [Django Vite](https://github.com/MrBin99/django-vite)
- [Django Inertia](https://github.com/inertiajs/inertia-django)
