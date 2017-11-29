# Ruby on Rails 5.1 Software Collection

This repository contains the code to package and maintain a Rails 5.1 Software Collection (SCL). The collection lives under the 'tfm-ror51' namespace.

### Requirements

 * ansible 2.4+
 * gem2rpm
 * copr-cli and copr credentials

## Adding a Package

To add a new package, begin by adding a new entry into the `package_manifest.yaml` including the name of the new package and the version desired. Now to add the spec file, git annex the source and create a branch with the changes:

```
ansible-playbook add_package.yml -l <package_name>
```

### Scratch Build

Updates to a package (or a new package) can be tested before submitting a pull request. Ensure that you have `copr-cli` set up and Copr credentials configured.

```
ansible-playbook scratch_build.yml -l <package_name>
```

This command will take the current state of the package locally and submit a build to Copr to generate a test build. You can then inspect the build logs through the Copr UI or download packages for runtime testing.

### Release Package

There is a job that handles automatic releasing of merge packages, however, in the event that this needs to be run by hand:

```
ansible-playbook release_package.yml -l <package_name>
```
