# RECONNAISANCE

> This phase deals with gathering as much information as possible about the target.

The more info you gather about the target, the more likely the next stages of the penetration test are successful.

2 types of recon:
  1. Passive recon.
  2. Active recon.
  
## 1. `Passive recon`
Is the process of gathering info about a target without any direct interaction with it.

### Passive recon tools and techniques.
 1. **Whois**

Is a TCP-based query/response protocol that is used to provide information services to internet users, usually about registered domain names.

This record contains information about the person or company that registers a domain name such as:
   1. Registrant information (owner of the domain).
   2. Registrar information (Organization that registered the domain).
   3. Registration dates.
   4. Name servers.
   5. Most recent update.
   6. Expiration dates.
   
whois can be used both online via [https://whois.domaintools.com/](https://whois.domaintools.com/) and on terminal via eg `whois google.com`.

 2. **GitHub**

Checking code hosting platforms is important because online stored source codes can provide information about the programming languages and frameworks that are used by the target.

Devs may accidentally add sensitive data or credentials to public repositories.

 3. **Stackoverflow**

Checking programming question-and-answer platforms is important because the developers might add an important part of the source code in their questions or the used programming languages and frameworks can be identified from the target's developers questions as in [stackoverflow](https://stackoverflow.com/)

 4. **Google Hacking / Google Dorking**

This is using advanced search queries in the google search engine to find vulnerable systems or sensitive infomation disclosures.

[The Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database) is a collection of search terms that have been used to reveal sensitive data exposed by vulnerable servers and web applications.

 5. **Netcraft**

[Netcraft](https://www.netcraft.com/) is an internet services company that tracks websites, it provides information about the infrastructure and technologies used by the target's websites.

 6. **Crunchbase**

[Crunchbase](https://www.crunchbase.com/) is a platform for finding business information about companies.

 7. **The Harvester**

Is an OSINT tool that gathers information such as emails, names, hosts, subdomains, IPs and URLs using multiple public data sources.

 8. **Shodan**

[Shodan](https://www.shodan.io/) is a search engine for Internet-connected devices and it can be used to identify the services/technologies used by those devices.

 9. **Censys**

[Censys](https://censys.io/) is a public search engine that enables researchers to discover, monitor and analyze devices that are accessible from the internet.

 10. **Sherlock**

[Sherlock](https://sherlock-project.github.io/) is a command line tool that can be used to find people across many sites using their usernames.

 11. **OSINT Framework**

[OSINT Framework](https://osintframework.com/) is a big collection of OSINT tools or resources.

### 2. `Active Recon`
Involves direct interaction with the target.
