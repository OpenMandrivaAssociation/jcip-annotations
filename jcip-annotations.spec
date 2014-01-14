%{?_javapackages_macros:%_javapackages_macros}
Name:           jcip-annotations
Version:        1
Release:        8.20060626.0%{?dist}
Summary:        Java annotations for multithreaded software


License:        CC-BY
URL:            http://www.jcip.net/
Source0:        http://www.jcip.net/%{name}-src.jar
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/net/jcip/%{name}/1.0/%{name}-1.0.pom

# There is no point in building native libraries, as the sources contain only
# annotation definitions, so no code would be generated.
BuildArch:      noarch
BuildRequires:  java-devel >= 1.5.0, jpackage-utils

Requires:       java >= 1.5.0, jpackage-utils


%description
This package provides class, field, and method level annotations for
describing thread-safety policies.  These annotations are relatively
unintrusive and are beneficial to both users and maintainers.  Users can see
immediately whether a class is thread-safe, and maintainers can see
immediately whether thread-safety guarantees must be preserved.  Annotations
are also useful to a third constituency: tools.  Static code-analysis tools
may be able to verify that the code complies with the contract indicated by
the annotation, such as verifying that a class annotated with @Immutable
actually is immutable.

%package javadoc

Summary:        Javadoc for jcip-annotations
Requires:       %{name} = %{version}-%{release}, jpackage-utils

%description javadoc
Javadoc documentation for the jcip-annotations package.
On systems where javadoc is sinjdoc, this package contains nothing useful
since sinjdoc does not understand annotations.

%prep
%setup -q -c

# Get rid of the manifest created upstream with ant
rm -fr META-INF

# Fix DOS line endings
sed -i 's/\r//' net/jcip/annotations/package.html

%build
mkdir classes
find . -name '*.java' | xargs %javac -g -source 1.5 -target 1.5 -d classes
cd classes
%jar cf ../%{name}.jar net
cd ..
%javadoc -d docs -source 1.5 net.jcip.annotations

%install
mkdir -p %{buildroot}%{_javadir}
mv %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# install maven metadata
mkdir -p %{buildroot}/%{_mavenpomdir}
cp %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# install javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-8.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-7.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-6.20060626
- Update to current packaging guidelines
- Resolves: rhbz#880283

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-5.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-4.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-3.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec  3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-2.20060626
- Fix maven metadata and pom filename (Resolves rhbz#655807)
- Use versionless jars and javadoc
- Few other packaging fixes

* Wed Jan  6 2010 Jerry James <loganjerry@gmail.com> - 1-1.20060626
- Add maven depmap
- Upstream uploaded a new source jar with a trivial difference
- Fix the version-release number

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-20060628.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-20060627.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May  5 2008 Jerry James <loganjerry@gmail.com> - 0-20060626.4
- Don't package source or HTML files in the jar

* Fri Apr 18 2008 Jerry James <loganjerry@gmail.com> - 0-20060626.3
- Changes required by new Java packaging guidelines

* Wed Nov 14 2007 Jerry James <loganjerry@gmail.com> - 0-20060626.2
- Don't make the javadocs appear in a docs subdirectory

* Tue Sep 18 2007 Jerry James <loganjerry@gmail.com> - 0-20060626.1
- Initial RPM
