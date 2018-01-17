# Django API + VueJS Frontend Proof-of-Concept

This is a proof of concept webservice + VueJS app using cross-domain cookies for authentication. It has a working
example of a Django API backend along with a VueJS 2.x frontend project based on the
[Vue webpack template](https://github.com/vuejs-templates/webpack).  This README will explain the high points of
getting this to work.

## API Backend

### Overview

The backend consists of a single
[@login_required](https://docs.djangoproject.com/en/1.11/topics/auth/default/#the-login-required-decorator) backend that
returns a JSON objects containing the current username. It uses Django's built-in auth system with a single user (name
`testuser` and password `testpass`, if using the included Dockerfile `api.Dockerfile`).

Django's settings allow cross-domain cookies and redirecting to another domain after login, but for manipulating
access control headers [django-cors-headers](https://github.com/ottoyiu/django-cors-headers) is necessary.

### Configuration

The API requires the following environment variables:
- `DEBUG_MODE` for [DEBUG](https://docs.djangoproject.com/en/1.11/ref/settings/#debug)
- `ALLOWED_HOSTS` is a comma-separated list to be used for
[ALLOWED_HOSTS](https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts)
- `SESSION_COOKIE_DOMAIN` for
[SESSION_COOKIE_DOMAIN](https://docs.djangoproject.com/en/1.11/ref/settings/#session-cookie-domain)
- `CSRF_COOKIE_DOMAIN` for
[CSRF_COOKIE_DOMAIN](https://docs.djangoproject.com/en/1.11/ref/settings/#csrf-cookie-domain)
- `LOGIN_REDIRECT_URL` for
[LOGIN_REDIRECT_URL](https://docs.djangoproject.com/en/1.11/ref/settings/#login-redirect-url)
- `FRONTEND_RESOURCES_DOMAIN` for [django-cors-headers](https://github.com/ottoyiu/django-cors-headers)'s
[CORS_ORIGIN_WHITELIST](https://github.com/ottoyiu/django-cors-headers#cors_origin_whitelist)

This granularity is required because of the way that Chrome (and presumably other browsers) handle cookies for 
`localhost`;  see [config/api.local.env](config/api.local.env) and [config/api.local.env](config/api.prod.env).

### Hosting

The API includes a pretty standard Dockerfile for this kind of app; see [api.Dockerfile](api.Dockerfile).

### OpenShift Configuration Examples

See the [openshift/](openshift) directory for example OpenShift resources for testing a production-like environment
using the OpenShift Container Platform.

## VueJS Frontend

The frontend is based on [VueJS](https://vuejs.org/), an incrementally-adoptable frontend framework suitable for
building complex apps.  It uses [Vue's webpack template](https://github.com/vuejs-templates/webpack), created as normal
using the [Vue command line tools](https://github.com/vuejs/vue-cli).

Most of this can be copied over without much ceremony (just make sure to pay attention to merge your `.gitignore`
files).

Beyond that, the following changes have been made:
- Moved `index.html` and `src/` into the `frontend/` folder for a little more organization
- Modified `config/webpack.{base,dev,prod}.conf.js` to account for these changes
- Added a `__API_URL__` entry for [DefinePlugin](https://webpack.js.org/plugins/define-plugin/) in
`config/webpack.{dev,prod}.conf.js` to use a different API URL for the local and production builds
- Modified my ESLint rules to require semicolons and disallow spaces before the first function paren :)

### Hosting

The frontend project has a Dockerfile so that it can be hosted as a container; see
[frontend.Dockerfile](frontend.Dockerfile) for details.  This could be improved by doing the actual production
frontend build in a CI tool like Jenkins (that way we wouldn't need NodeJS or NPM in the production container), but
this way works for demonstration purposes.

### Further Reading

See also:
- [VueJS Webpack Guide](http://vuejs-templates.github.io/webpack/)
- [vue-loader Documentation](http://vuejs.github.io/vue-loader).

## Still TBD

The following things still need some work:
- Replace `fetch` on the frontend with [Axios](https://github.com/axios/axios); think about a
[mixin](https://vuejs.org/v2/guide/mixins.html)
- Test in iframes (also multiple browsers -- Safari in particular)
- Modify `CORS_ORIGIN_WHITELIST` settings to allow env var csv like `ALLOWED_HOSTS`, but required
