# TypoDetect

This tool gives blue teams, SOC's, researchers and companies
the ability to detect the active mutations of their domains, 
thus preventing the use of these domains in fraudulent 
activities, such as phishing and smishing.

For this, Typodetect allows the use of the latest available
version of the TLDs (Top Level Domains) published on the 
IANA website, the validation of decentralized domains in 
Blockchain DNS and the malware reports in DoH services 
(DNS over HTTPS) .

For the ease of the user, Typodetect delivers the report 
in JSON format by default, or in TXT format, depending on 
how the user selects and shows on the screen a summary of 
the mutations generated, the active domains and the reports
detected with Malware or decentralized domains.

---

## Installation

Clone this repository with:
```bash
git clone https://github.com/ElevenPaths/typodetect
```

Run setup for installation:

```bash
python3 pip install -r requirements.txt
```

### Running TypoDetect

Inside the TypoDetect directory:

```bash
python3 typodetect.py -h
```

```bash
usage: typodetect.py [-h] [-u UPDATE] [-t N_THREADS] [-d DOH_SERVER] [-o OUTPUT] domain

positional arguments:
  domain                specify domain to process

optional arguments:
  -h, --help            show this help message and exit
  -u UPDATE, --update UPDATE
                        (Y/N) for update TLD's database (default:N)
  -t N_THREADS, --threads N_THREADS
                        Number of threads for processing (default:5)
  -d DOH_SERVER, --doh DOH_SERVER
                        Section DoH for use: [1] ElevenPaths (default) [2] Cloudfare
  -o OUTPUT, --output OUTPUT
                        JSON or TXT, options of filetype (default:JSON)
```

For a simple analysis:

```bash
python3 typodetect.py <domain>
```

For update IANA database and analysis:

```bash
python3 typodetect.py -u y <domain>
```

For more threads analysis:

```bash
python3 typodetect.py -t <number of threads> <domain>
```

For a different DoH (currently only has ElevenPaths o CloudFare)

```bash
python3 typodetect.py -d 2 <domain>
```

For create TXT report

```bash
python3 typodetect.py -o TXT <domain>
```

### Reports

Inside the reports directory, the report file is saved,
by default in JSON, with the name of the analyzed 
domain and the date, for example:

```bash
elevenpaths.com2021-01-26T18:20:10.34568.json
```

The JSON report has the following structure for each active mutation detected:

```bash
{ id: 
    "report_DoH" : <string>
    "domain": <string>
    "A": [ip1, ip2, ...]
    "MX": [mx1, mx2, ...]
    }
```

The fields contain the following information:

```bash
id: Integer id of mutation
"report_DoH": ""        - Domain of Descentralised DNS
              "Malware" - Domain reported as dangerous for DoH
              "Good"    - Domain reported as good for DoH
"domain": Mutation detected as active.
"A": IP's address of A type in DNS of the mutation.
"MX": IP's or CNAME of MX type in DNS of the mutation.
```



### More info

**Wiki:** [https://innovation-gitlab.e-paths.com/private/typodetect/-/wikis/TypoDetect](https://innovation-gitlab.e-paths.com/private/packagedna/-/wikis/TypoDetect

