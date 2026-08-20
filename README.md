# odoo-submodule-hello-word

Minimal "Hello World" Odoo 19 module, meant to be added as a Git submodule
to an [Odoo.sh](https://www.odoo.sh) project.

## What it does

Installs a `hello_world` module that exposes a public HTTP route:

```
GET /hello  ->  "Hello, World!"
```

No models, no views, no security rules — just a controller and its test.

## Repository layout

```
hello_world/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── main.py          # /hello route
└── tests/
    ├── __init__.py
    └── test_hello.py    # HttpCase test for /hello
```

## Deploying on Odoo.sh

1. Push this repository to GitHub (private or public).
2. In your Odoo.sh project, go to **Settings → Submodules → Add**.
3. Paste the repository's SSH clone URL and the branch to track (e.g. `main`).
   For a private repository, add the deploy key Odoo.sh shows you to the
   repository's **Settings → Deploy keys** on GitHub.
4. Odoo.sh commits the submodule to your project repository and rebuilds.
5. On a development branch build, install the **Hello World** module from
   the Apps menu (enable developer mode and update the apps list first),
   or add `hello_world` to the branch's install list.
6. Open `https://<your-build-url>/hello` — you should see `Hello, World!`.

Alternatively, add the submodule manually from your Odoo.sh project clone:

```bash
git submodule add <ssh-clone-url> hello-world
git commit -m "chore: add hello_world submodule"
git push
```

Odoo.sh detects any folder containing a `__manifest__.py` inside the
submodule as an installable module.

## Running tests

Odoo.sh runs the module's tests automatically on development branch builds
(check the build's logs). To run them locally with Docker:

```bash
docker network create odoo-hello-net
docker run -d --name odoo-hello-pg --network odoo-hello-net \
  -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres \
  postgres:16-alpine
docker run --rm --network odoo-hello-net \
  -e HOST=odoo-hello-pg -e USER=odoo -e PASSWORD=odoo \
  -v "$(pwd)/hello_world:/mnt/extra-addons/hello_world" \
  odoo:19 odoo -d hello_test -i hello_world \
  --test-tags /hello_world --stop-after-init --log-level=test
```
