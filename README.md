# Django with Vite and Inertia

Set up your Django project with Vite and Inertia.

Other configurations:

- Database (PostgreSQL, SQLite)
- Vue
- Tailwind CSS (optional)
- Docker (optional)
  - Development
  - Production

## Getting started

- Using [uv](https://docs.astral.sh/uv/) (Recommended)

```bash
mkdir awesome-project
uvx copier copy gh:sarthakjariwala/django-vite-inertia awesome-project
```

- Alternatively, you may have installed [copier](https://copier.readthedocs.io/en/stable/) through other means such as `pipx`, etc.

```bash
mkdir awesome-project
copier copy gh:sarthakjariwala/django-vite-inertia awesome-project
```

## Update project template

You can also get the latest changes in your project as this template evolves in the future.

```bash
cd awesome-project
uvx copier update
```

Or

```bash
cd awesome-project
copier update
```

---

> Note: If you don't want to use Vue, you can still generate the project using this template and replace Vue specific files with React or Svelte or any other frontend supported by Inertia.
