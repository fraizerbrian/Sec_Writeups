# OWASP TESTING PROJECT SUMMARY

WSTG - Web Security Testing Guide

> Below is a compilation of some of the main points from the OWASP TESTING PROJECT

## What to test

An effective testing program should have components that test the following:
	1. People
	2. Process
	3. Technology

By testing the people, policies, and processes, an organization can catch issues that would later manifest themselves into defects in the technology, thus eradicating bugs early and identifying the root causes of defects.

## Referencing WSTG Scenarios

Format:
```
WSTG-<CATEGORY>-<NUMBER>

		where;	**category** is a 4 character upper case string that identifies the type of test or weakness
						**number** is a zero-padded numeric value from 01-99
		eg: WSTG-INFO-02 ie the second information gathering test
```

Format 2:
```
WSTG-<version>-<category>-<number>
		
		Where; **version** is the version tag
		eg: WSTG-v42-INFO-02 ie second information gathering test from version 4.2
```

## Principles of Testing
1. There is no silver bullet

2. Think strategically, not tactically
- Patch-and-penetrate model involves fixing a reported bug, but without proper investigation of the root cause and is associated with the window of the vulnerability ie **Window Of Exposure**

3. The SDLC is King
- Build security into the SDLC to prevent reoccurring security problems within an application.
- Security can be built into the SDLC by developing standard, policies and guidelines that fit and work within the development methodology.
- Each conceptual phase of the archetype SDLC will be used to develop the application ie:
		1. Define
		2. Design
		3. Develop
		4. Deploy
		5. Maintain

4. Test Early and Test Often
- When a bug is detected early within the SDLC it can be addressed faster and at a lower cost.
- Education in security testing also helps developers acquire the appropriate mindset to test an application from an attacker’s perspective.

5. Test Automation
- In modern development methodologies such as: _agile, devops/devsecops, or rapid application development (RAD)_ consideration should be put into integrating security tests in to continuous integration/continuous deployment (CI/CD) workflows in order to maintain baseline security information/analysis and identify “low hanging fruit” type weaknesses.
- Leverage on:
		1. Dynamic Application Security Testing (DAST)
		2. Static Application Security Testing (SAST)
		3. Software Composition Analysis (SCA)

6. Understand the scope of security
- kNow how much security a given project will require. 
- Assets are classified according to how they should be handled ie; _Confidential, Secret, top secret_
- Discussions should occur with legal council to ensure that any specific security requirements will be met.

7. Develop the right mindset
- Successfully testing an application for security vulnerabilities requires thinking “outside of the box.”
- Good security testing requires going beyond what is expected and thinking like an attacker who is trying to break the application.
- Creative thinking can help to determine what unexpected data may cause an application to fail in an insecure manner.
- It can also help find any assumptions made by web developers that are not always true, and how those assumptions can be subverted.

8. Understand the subject
- Require accurate documentation of the application
- Have at least a basic security infrastructure that allows the monitoring and trending of attacks against an organization’s applications and network (e.g., intrusion detection systems).

9. Use the right tools
- Tools can simplify and speed up the security process by assisting security personnel in their tasks. However, it is important to understand exactly what these tools can and cannot do so that they are not oversold or used incorrectly.

10. The devil is in the details
- Review the findings and get rid of false positives that may remain in the report.
- Verify that every possible section of application logic has been tested, and that every use case scenario was explored for possible vulnerabilities.

11. Use source code when available
- While black-box penetration test results can be impressive and useful to demonstrate how vulnerabilities are exposed in a production environment, they are not the most effective or efficient way to secure an application.
- It is possible to discover vulnerabilities within the application source that would be missed during a black-box engagement.

12. Develop Metrics
- Track the results of testing engagements, and develop metrics that will reveal the application security trends within the organization.
- Good metrics will show:
		1. If more education and training are required;
		2. If there is a particular security mechanism that is not clearly understood by the development team
		3. If the total number of security related problems being found is decreasing.

13. Document the test results
- Produce a formal record of what testing actions were taken, by whom, when they were performed, and details of the test findings. 
- Agree on an acceptable format for the report that is useful to all concerned parties, which may include developers, project management, business owners, IT department, audit, and compliance.
- The report should clearly identify to the business owner where material risks exist, and do so in a manner sufficient to get their backing for subsequent mitigation actions. 
- The report should also be clear to the developer in pin-pointing the exact function that is affected by the vulnerability and associated recommendations for resolving issues in a language that the developer will understand.
- The report should also allow another security tester to reproduce the results.

## Testing Techniques
1. Manual Inspections & Reviews
2. Threat Modelling
3. Code Review
4. Penetration Testing
