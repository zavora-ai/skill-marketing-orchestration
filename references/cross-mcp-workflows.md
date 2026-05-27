# Marketing Cross-MCP Workflows

## Marketing + CRM: Lead → Nurture → Convert
```
CRM: search_contacts(segment: "trial_expired") → leads
MARKETING: create_audience(from_contacts: leads)
MARKETING: create_campaign(name: "Win-back", audience_id)
MARKETING: send_campaign_email(campaign_id, audience_id)
MARKETING: get_campaign_metrics(id) → {conversions: 12}
CRM: update_contacts(converted_ids, stage: "Reactivated")
```

## Marketing + Analytics: Attribution → Budget Shift
```
MARKETING: get_attribution() → {linkedin: 45% of conversions, google: 30%, email: 25%}
MARKETING: get_channel_comparison() → {linkedin_roas: 4.2, google_roas: 2.1}
MARKETING: allocate_budget(from: "google", to: "linkedin", amount: 2000)
SLACK: send_message(channel: "#marketing", text: "📊 Budget shifted: +$2k to LinkedIn (4.2x ROAS vs Google 2.1x)")
```
