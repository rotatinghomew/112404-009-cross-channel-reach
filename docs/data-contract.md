# 合成资料约定

资料用于本地业务流程演练，字段仅记录事实来源，不预先裁定业务结果。

- `channels.csv`：展览讲解入口及启停时间。字段为 `channel_id, channel_type, exhibit_id, active_from, active_to, entry_context, campaign_ref`。
- `events.csv`：入口曝光、阅读、播放和反馈事件，参与者代号仅用于演练。字段为 `event_id, channel_id, visitor_token, language, age_band, event_at, event_type, content_id, consent_state, session_key`。
- `aggregation_requests.csv`：受众切片请求及发布状态。字段为 `request_id, period, dimension_set, minimum_group, requested_by, state, created_at`。
- `venue_counts.csv`：馆内场次客流和讲解活动签到汇总，用于与数字渠道口径对照。字段为 `record_id, exhibit_id, gallery_id, period, visitors, guided_visitors, measurement, source_ref`。

空字段表示事实尚未提供，`pending`、`review`、`hold` 等状态表示来源记录尚未形成最终确认。不同来源以事件日期或有效期表达的时间含义不相同，调用方应结合表名和字段解释；不能仅因编号相同就假定两条记录可合并。金额以资料中记载的名义单位表示，没有统一换算或预先扣除退款。
