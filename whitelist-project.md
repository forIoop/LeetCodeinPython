# CM-08 Whitelist
The CM-08 whitelist is an on platform solution for streamlining the whitelist validation process
needed for the build and installation of our servers.
This application provides a central and secure environment where you can change and query
the whitelist and dynamically update those changes in our PuppetMaster repo.

![CM-08 Whitelist Diagram](./images/CM-08%20Whitelist.svg "CM-08 Whitelist Diagram")


### Background
Every time a server on our system is installed its package inventory must validated through
a whitelist (list of authorized packages that server can install). Originally, This whitelist
is a static .txt file in our puppet master repo. In order to push any sort of change to this file
you must do the following:
1. Manually update change in whitelist file
2. Commit changes and hold a code review
3. Wait for merge / approval
4. Wait for Cron Job to run puppet script (This process takes about an hour for changes to update)

Additionally, if whitelist validation fails our servers will receive unwanted alerts and errors related
to the build process. Originally, we had to resort to workarounds for these alerts (Things like
temporarily disabling our whitelist file) in order for our builds to run successfully.

### Solution
In order to streamline the entire whitelist validation process we need to achieve the following:
* Create a central place where we can interact and modify our whitelist
* Maintain a secure environment where we can manage whitelist information
* Implement a consistent system that ensures any server is equipped with the authorized software it needs

### User Stories
A list of user's perspectives and use cases regarding the benefits of our CM-08 Whitelist

1. (Systems Engineer): As a Systems Engineer, I would like a central place where I can add,
 edit, and query whitelisted packages so that I can streamline the entire whitelist
 validation process.
 
2. (Security Solutions Architect): As a Security Solutions Architect, I would like an environment
 where I can validate and secure whitelist package information so that I can ensure
 our infrastructure runs safely.

3. (Systems Administrator): As a Systems Administrator, I would like an interface where I
can scan for whitelist build failures so that I can ensure the whitelist validation
process is reliable.

4. (Auditor): As an Auditor, I need to ensure that any authorized software installation I
choose for an audit is consistent with all of the packages in my server.

5. (Site Reliability Engineer): As a site reliability engineer, I would like to receive 
real time alerts whenever one of my servers are built with unauthorized packages.

### High Level Overview
#### Phase 1:
Phase 1 consists of the minimum features needed for our CM-08 Whitelist to be accepted
and utilized. Below is a high level overview of our MVP implementation and testing:

Implementation:
1. Import whitelist data into Data Center Dev environment
2. Created scoped app on platform and tablelize data
3. Modify / Query table data and export
4. Create REST API GET request to table endpoint so that it returns the entire whitelist
5. Parse JSON object into a .txt file
6. Pass in .txt file into Cron Job in order to build file at a new location in puppet master repo.

Testing:
* Unit tests are needed in order to validate the transaction from platform to REST API, ensure
JSON object is parsed and built correctly into a .txt file, and confirm Cron Job is able to utilize
the file.
* Integration tests are needed in order to verify that the newly built whitelist in PuppetMaster repo
is identical to the one on platform.
* Regression tests are needed in order to assert that the new whitelist build process does not have any
adverse affects on the original puppet script which preforms the Cron Job

#### Phase 2:
Phase 2 consists of extra features that can make our whitelist process more extensive and reliable.
Below are possible ideas of phase 2 features:
* Create a schema for our table with different fields (env, fileType, name)
* Create on platform option to export as a txt file (so parsing is not needed)
* Create config file in order to store variables such as:
[DestinationDirectory][Connection Server][filename][filetype]

#### Phase 3:
Phase 3 consists of security features that make our whitelist process safer and more restrictive.
Below are possible ideas of phase 3 features:
* Restrict permissions of access to on platform scoped app
* Raise an error to REST API if fileType is not app/db
* Raise an error if we encounter a * in our list (we cannot have a star because tha wil
