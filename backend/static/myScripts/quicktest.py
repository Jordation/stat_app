from Format_MatchOBJ import createToken



def returnXY(fields, data):
    def forEach(inner_data, param):
        t1 = [i[param] for i in inner_data['t1_c']]
        t2 = [i[param] for i in inner_data['t2_c']]
        t1.extend(t2)
        return t1

    mapnum = f"m{fields['mapnum']}_data"
    ret_x = forEach(data[mapnum], fields['x'])
    ret_y = forEach(data[mapnum], fields['y'])
    return ret_x, ret_y


def main():
    url = "https://www.vlr.gg/157757/edward-gaming-vs-nter-xyper-arena-weekly-showdown-4-uf"
    data = createToken(url)['data']
    xy = returnXY({'mapnum': '1', 'x': 'Kills', 'y': 'Player'}, data)
    print(xy)

if __name__ == '__main__':
    main()
