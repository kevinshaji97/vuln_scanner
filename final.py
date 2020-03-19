import scanner

target_url = "http://192.168.1.6/mutillidae/"

vuln_scanner = scanner.Scanner(target_url)
vuln_scanner.crawl(target_url)