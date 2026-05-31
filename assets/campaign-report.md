# Campaign Report Template

Use this structure when presenting marketing campaign results.

---

## 📣 {campaign_name}

**Channel:** {channel} | **Status:** {status_emoji} {status} | **Period:** {start_date} — {end_date}

### Performance Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Impressions | {impressions} | {target_impressions} | {imp_status} |
| Clicks | {clicks} | {target_clicks} | {click_status} |
| CTR | {ctr}% | {target_ctr}% | {ctr_status} |
| Conversions | {conversions} | {target_conversions} | {conv_status} |
| Cost | ${spend} | ${budget} | {budget_status} |
| CPA | ${cpa} | ${target_cpa} | {cpa_status} |

{status indicators: ✅ On Track, ⚠️ Below Target, 🌟 Exceeding}

### Audience Breakdown

| Segment | Reach | Engagement |
|---------|-------|-----------|
| {segment_name} | {segment_reach} | {segment_engagement}% |

### ROI Summary

| Metric | Value |
|--------|-------|
| Revenue Attributed | ${revenue} |
| ROAS | {roas}x |
| Pipeline Generated | ${pipeline_value} |

{if ctr < target_ctr: "⚠️ CTR below target — review creative and targeting"}
{if roas > 3: "🌟 Strong ROAS — consider scaling budget"}
{if spend > budget: "🚨 Over budget — pause or reduce bids"}

---

*Generated from mcp-marketing | {timestamp}*
