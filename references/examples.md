# Marketing Examples

## Example 1: "Launch a campaign targeting CTOs"
```
create_audience(criteria: {role: "CTO", company_size: ">100"}) → {size: 8500}
create_campaign(name: "Enterprise Q1", channels: ["linkedin", "email"], budget: 5000)
create_content(type: "linkedin_ad", headline: "Ship 10x faster with AI agents")
launch_campaign(id)
```
Response: "✅ Campaign live: Enterprise Q1 targeting 8,500 CTOs on LinkedIn + Email. Budget: $5,000."

## Example 2: "How's our campaign performing?"
```
get_campaign_metrics(id) → {impressions: 45000, clicks: 2100, conversions: 85, roas: 3.8}
get_channel_comparison() → {linkedin: {ctr: 4.7%}, email: {open_rate: 32%}}
```
Response: "Campaign: 45k impressions, 2.1k clicks (4.7% CTR), 85 conversions. ROAS: 3.8x. LinkedIn outperforming email."
