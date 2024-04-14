-- graduate_personal_stat/network_flow_equivalence
-- 计算流量相当于看了多少甄嬛传（按 167GB 计算）

UPDATE graduate_personal_stat
SET network_flow_equivalence = CAST(network_flow AS REAL) / 167
WHERE network_flow IS NOT NULL;
