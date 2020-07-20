%{?python_enable_dependency_generator}
%global pypi_name importlib_resources

%global desc \
importlib_resources is a backport of Python 3.7's standard library\
importlib.resources module for 3.4 through 3.6. Users of Python 3.7 and\
beyond should use the standard library module, since for these\
versions, importlib_resources just delegates to that module.


Name:           python-importlib-resources
Version:        3.0.0
Release:        1%{?dist}
Summary:        Read resources from Python packages

License:        ASL 2.0
URL:            https://importlib-resources.readthedocs.io/
Source0:        %pypi_source

Patch0001: 0001-raise-NotImplementedError-on-Python-2.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-zipp
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(wheel)

%description %{desc}

%package -n     python3-importlib-resources
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-importlib-resources %{desc}

%package doc
Summary:        importlib_resources documentation
%description doc
Documentation for importlib_resources

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
sed -i '/setup_requires/d' setup.cfg

%build
%py3_build
# Skip doc build, needs new deps python-rst-linker, python-jaraco-packaging
# generate html docs
#PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-importlib-resources
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files doc
%license LICENSE
%doc README.rst

%changelog
* Mon Jul 20 2020 Yatin Karel <ykarel@redhat.com> - 3.0.0-1
- Update to 3.0.0
- Also update NotImplemented Python2 patch
- Skip docs build

* Fri Mar 20 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.2-2
- Rebuild again for EPEL 8

* Thu Nov 07 2019 Ken Dreyer <kdreyer@redhat.com> - 1.0.2-1
- Initial package.
