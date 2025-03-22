def create_table(teams, dates):
    out = """
<table>
<tr>
{headers}
</tr>
{rows}
</table>
    """
    out = out.replace("{headers}", create_headers(dates))

    rows = ""
    for team in teams:
        rows += create_row(team)
    out  = out.replace("{rows}", rows)

    return out


def create_headers(dates):
    headers = """<th>Lag</th>
<th>Totalt</th>"""
    for date in dates:
        headers += f"\n<th>{date}</th>"
    return headers

def create_row(team):
    out = f"""<tr>
<td>{team.name}</td>
<td>{format_points(team.points_total)}</td>"""
    
    for points in team.points_list:
        out += f"\n<td>{format_points(points)}</td>"
    out += "\n</tr>"

    return out

def format_points(points):
    if points == points // 1:
        return round(points)
    return round(points, 1)