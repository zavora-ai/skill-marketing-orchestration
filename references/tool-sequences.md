# Marketing Tool Sequences (22 tools)

## Campaigns (5): list, get, create, launch, pause
## Audiences (4): list, get, create, estimate_reach
## Content (4): list, create, get_ab_variants, get_content_calendar
## Channels (4): list, schedule_post, create_ad, send_campaign_email
## Performance (3): get_campaign_metrics, get_attribution, get_channel_comparison
## Budget (2): get_budget_status, allocate_budget

## Sequence: Full Campaign Launch (5 calls)
```
1. create_audience(criteria: {interest: "SaaS", role: "CTO"}) → {id, size: 12000}
2. create_campaign(name: "Q1 Enterprise Push", channels: ["email", "linkedin"], audience_id, budget: 5000)
3. create_content(campaign_id, type: "email", subject: "...", body: "...")
4. get_budget_status() → verify budget available
5. launch_campaign(id) → active across channels
```
