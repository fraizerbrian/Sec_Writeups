# OWASP

Resources : [OWASP](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/00-Introduction_and_Objectives/README)

OWASP approach creates a defined Testing Methodology that will be _consistent_, _reproducible_, _rigorous_ and _under quality control_.

The OWASP Web Application Security Testing method is based on the **black box** approach ie tester knows nothing or has very little information about the application to be tested.

Testing model consists of:

	1. Tester : Who performs the testing activities
	2. Tools and Methodology : Testing guide project
	3. Application: Black box to test

## Passive Testing

> Tester tries to understand the application's logic and explores the application as a user.

Tools can be used for information gathering.

At the end of this phase the tester should understand all the access points and functionality of the system such as HTTP headers, parameters, cookies, APIs, technology usage/patterns etc.

## Active Testing

Tester begins to use the methodologies described in the following sections.

	1. Information gathering
	2. Configuration and Deployment Management Testing
	3. Identity Management Testing
	4. Authentication Testing
	5. Authorization Testing
	6. Session Management Testing
	7. Input Validation Testing
	8. Error Handling
	9. Cryptography
	10. Business Logic Testing
	11. Client-side Testing
	12. API Testing

------------------------------------------------------------------------------------------------
## CHECKLIST

- [ ] Introduction
	- [ ] OWASP testing project
	- [ ] Principles of Testing
	- [ ] Testing Techniques Explained
	- [ ] Manual Inspections and Reviews
	- [ ] Threat Modeling
	- [ ] Source code reviews
	- [ ] Penetration Testing
	- [ ] Need for a balanced approach
	- [ ] Deriving security test requirements.
	- [ ] Security tests integrated in development and testing workflows.
	- [ ] Security Test Data Analysis and Reporting.
- [ ] The OWASP Testing Framework
	- [ ] The Web Security Testing Framework
	- [ ] Phase 1 Before Development Begins
	- [ ] Phase 2 During Definition and Design
	- [ ] Phase 3 During Development
	- [ ] Phase 4 During Deployment
	- [ ] Phase 5 During Maintenance and Operations
	- [ ] A Typical SDLC Testing Workflow
	- [ ] Penetration Testing Methodologies
- [ ] Web Application Security Testing
	- [ ] Information Gathering
		- [ ] Conduct Search Engine Discovery Recon for info leakage
		- [ ] Fingerprint web server
		- [ ] Review webserver metafiles for information leakage
		- [ ] Enumerate applications on web server
		- [ ] Review webpage content for information leakage
		- [ ] Identify application entry points
		- [ ] Map Execution paths through application
		- [ ] Fingerprint web application framework
		- [ ] Fingerprint web application
		- [ ] map application architecture
	- [ ] Configuration and Deployment management testing
		- [ ] Test Network infrastructure configuration.
		- [ ] Test application platform configuration.
		- [ ] Test file extensions handling for sensitive information.
		- [ ] Review old backup and unreferenced files for sensitive information.
		- [ ] Enumerate infrastructure and application admin interfaces.
		- [ ] Test HTTP methods.
		- [ ] Test HTTP Strict Transport Security.
		- [ ] Test RIA Cross Domain Policy.
		- [ ] Test File Permission.
		- [ ] Test for subdomain takeover.
		- [ ] Test Cloud storage.
	- [ ] Identity Management Testing
		- [ ] Test Role Definitions.
		- [ ] Test User Registration Process.
		- [ ] Test account provisioning process.
		- [ ] testing for account enumeration and guessable user account.
		- [ ] testing for weak or unenforced username policy.
	- [ ] Authentication Testing
		- [ ] Testing for credentials transported over an encrypted channel.
		- [ ] Testing for default credentials.
		- [ ] Testing for weak lock out mechanism.
		- [ ] Testing for bypassing authentication schema.
		- [ ] Testing for vulnerable remember password.
		- [ ] Testing for browser cache weakness.
		- [ ] Testing for weak password policy.
		- [ ] Testing for weak security question answer.
		- [ ] Testing for weak password change or reset functionalities.
		- [ ] Testing for weaker authentication in alternative channel.
	- [ ] Authorization Testing
		- [ ] Testing Directory Traversal file include.
		- [ ] Testing for bypassing authorization schema.
		- [ ] Testing for privilege escalation.
		- [ ] Testing for insecure direct object references.
	- [ ] Session Management Testing
		- [ ] Testing for session management schema.
		- [ ] Testing for cookies attributes.
		- [ ] Testing for session fixation.
		- [ ] Testing for exposed session variables.
		- [ ] Testing for cross site request forgery.
		- [ ] Testing for logout functionality.
		- [ ] Testing session timeout.
		- [ ] Testing for session puzzling.
		- [ ] Testing for session hijacking.
	- [ ] Input Validation Testing
		- [ ] Testing for reflected cross site scripting.
		- [ ] Testing for stored cross site scripting.
		- [ ] Testing for HTTP verb tampering
		- [ ] Testing for HTTP parameter pollution.
		- [ ] Testing for SQL injection.
			- [ ] Testing for Oracle.
			- [ ] Testing for MySQL.
			- [ ] Testing for SLQ server.
			- [ ] Testing PostgreSQL.
			- [ ] Testing for MS Access.
			- [ ] Testing for NoSQL injection.
			- [ ] Testing for ORM injection.
			- [ ] Testing for client-side
		- [ ] Testing for  LDAP injection.
		- [ ] Testing for XML injection.
		- [ ] Testing for SSI injection.
		- [ ] Testing for XPath Injection.
		- [ ] Testing for IMAP SMTP injection.
		- [ ] Testing for code injection.
			- [ ] Testing for LFI.
			- [ ] Testing for RFI.
		- [ ] Testing for command injection.
		- [ ] Testing for format string injection.
		- [ ] Testing for incubated vulnerability.
		- [ ] Testing for HTTP splitting smuggling.
		- [ ] Testing for HTTP incoming Requests.
		- [ ] Testing for host header injection.
		- [ ] Testing for SSRF.
	- [ ] Testing for Error Handling.
		- [ ] Testing for improper error handling.
		- [ ] Testing for stack traces.
	- [ ] Testing for Weak Cryptography.
		- [ ] Testing for weak transport layer security(TLS).
		- [ ] Testing for padding oracle.
		- [ ] Testing for sensitive information sent via unencrypted channels.
		- [ ] Testing for Weak Encryption.
	- [ ] Business Logic Testing.
		- [ ] Intro.
		- [ ] Test business logic data validation.
		- [ ] Test ability to forge requests.
		- [ ] Test integrity checks.
		- [ ] Test for process timing.
		- [ ] Test number of times a function can be used limits.
		- [ ] Testing for the circumvention of work flows.
		- [ ] Test defenses against application misuse.
		- [ ] Test upload of unexpected file types.
		- [ ] Test upload of malicious files.
	- [ ] Client-side testing.
		- [ ] Testing for DOM-Based cross-site scripting.
		- [ ] Testing for Javascript execution.
		- [ ] Testing for HTML injection.
		- [ ] Testing for client-side url redirect.
		- [ ] Testing for CSS injection.
		- [ ] Testing for client-side resource manipulation.
		- [ ] Testing Cross origin resource sharing.
		- [ ] Testing for cross site flashing.
		- [ ] Testing for clickjacking.
		- [ ] Testing websockets.
		- [ ] Testing web messaging.
		- [ ] Testing browser storage.
		- [ ] Testing for cross site script inclusion.
	- [ ] API Testing.
		- [ ] Testing GraphQL
	- [ ] Reporting
	
