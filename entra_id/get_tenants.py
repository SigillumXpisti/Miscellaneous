import requests

domains = ["contoso.com"]

def get_tenant(domain):
    url1 = f"https://login.microsoftonline.com/common/userrealm/{domain}?api-version=2.1"
    url2 = f"https://login.microsoftonline.com/{domain}/.well-known/openid-configuration"
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)

    if response1.ok and response2.ok:
        data1 = response1.json()
        data2 = response2.json()
        
        federation_brand_name = data1.get('FederationBrandName')
        token_endpoint = data2.get('token_endpoint')
        tenant_id = token_endpoint.split("/")[3] if token_endpoint else None
        tenant_region_scope = data2.get('tenant_region_scope')

        if tenant_id:
            response3 = requests.get(f"https://azure-ad-tools.ai.moda/api/v1.0.0/lookup-by-tenant-id/{tenant_id}")
            data3 = response3.json()
            defaultDomainName = data3.get('defaultDomainName')
            print(f"{tenant_id},{tenant_region_scope},{defaultDomainName},{federation_brand_name},{domain}")

for domain in domains:
    get_tenant(domain)