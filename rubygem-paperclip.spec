# Generated from paperclip-2.3.8.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	paperclip

Summary:	File attachments as attributes for ActiveRecord
Name:		rubygem-%{rbname}

Version:	2.3.8
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://www.thoughtbot.com/projects/paperclip
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Easy upload management for ActiveRecord

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(.rb|rails|shoula_macros|test)'

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/init.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/generators/
%{ruby_gemdir}/gems/%{rbname}-%{version}/generators/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/rails
%{ruby_gemdir}/gems/%{rbname}-%{version}/rails/init.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/shoulda_macros
%{ruby_gemdir}/gems/%{rbname}-%{version}/shoulda_macros/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*

