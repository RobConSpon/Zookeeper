walk_h = int(input())
walk_m = int(input())
walk_s = int(input())
rain_h = int(input())
rain_m = int(input())
rain_s = int(input())
hour_diff = rain_h - walk_h
h_d_secs = hour_diff * 60 * 60
min_diff = rain_m - walk_m
m_d_secs = min_diff * 60
s_d_secs = rain_s - walk_s
total_secs = h_d_secs + m_d_secs + s_d_secs
print(total_secs)