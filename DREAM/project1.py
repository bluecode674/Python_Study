import random

player_health = 100  # 플레이어 체력
player_money = 0  # 플레이어 돈
monsters = [
    {"이름": "슬라임", "체력": 50, "공격력": 10, "보상_돈": 20},
    {"이름": "고블린", "체력": 80, "공격력": 15, "보상_돈": 40},
    {"이름": "드래곤", "체력": 150, "공격력": 20, "보상_돈": 100}
]
player_items = [
    {"이름": "무기", "공격력_증가": 10},
    {"이름": "방어구", "방어력_증가": 5},
    {"이름": "물약", "체력_회복량": 30}
]  # 플레이어 아이템
shop_items = [
    {"이름": "물약", "가격": 30, "체력_회복량": 30},
    {"이름": "마법 무기", "가격": 100, "공격력_증가": 20},
    {"이름": "강화 방어구", "가격": 150, "방어력_증가": 10}
]
has_rested = False  # 휴식 여부
has_visited_shop = False  # 상점 방문 여부

def battle():
    global player_health, player_money, has_rested, has_visited_shop
    
    print("\n==================================")
    print("          몬스터와 전투 시작         ")
    print("==================================\n")
    
    # 랜덤한 몬스터 선택
    monster = random.choice(monsters)
    monster_name = monster["이름"]
    monster_health = monster["체력"]
    monster_damage = monster["공격력"]
    reward_money = monster["보상_돈"]
    
    while player_health > 0 and monster_health > 0:
        print("==================================")
        print("   플레이어 체력:", player_health)
        print("   " + monster_name + " 체력:", monster_health)
        print("==================================\n")
        print("1. 공격하기")
        print("2. 아이템 사용하기")
        print("3. 도망가기")
        
        choice = input("\n행동을 선택하세요: ")
        
        if choice == "1":
            # 플레이어가 몬스터를 공격
            player_damage = random.randint(5, 20)  # 플레이어의 공격력
            print("\n플레이어가 몬스터를 공격합니다! 플레이어의 공격력:", player_damage)
            monster_health -= player_damage
            
            if monster_health <= 0:
                print("\n몬스터를 물리쳤습니다! 전투에서 승리하였습니다.")
                player_money += reward_money
                print(reward_money, "돈을 획득하였습니다.")
                break
            
            # 몬스터가 플레이어를 공격
            print("\n몬스터가 플레이어를 공격합니다! 몬스터의 공격력:", monster_damage)
            player_health -= monster_damage
            
            if player_health <= 0:
                print("\n플레이어가 사망하였습니다. 게임 오버입니다.")
                break
        
        elif choice == "2":
            # 아이템 사용
            print("\n가방을 엽니다.")
            print("가방 안에 있는 아이템 목록:")
            for i, item in enumerate(player_items):
                print(str(i+1) + ". " + item["이름"])
            
            item_choice = input("\n사용할 아이템의 번호를 선택하세요: ")
            
            if item_choice.isdigit() and int(item_choice) <= len(player_items):
                selected_item = player_items[int(item_choice) - 1]
                print("\n" + selected_item["이름"] + "을(를) 사용합니다.")
                
                if "체력_회복량" in selected_item:
                    player_health += selected_item["체력_회복량"]
                    print("체력이 회복되었습니다. 현재 체력:", player_health)
                elif "공격력_증가" in selected_item:
                    # 공격력 증가에 대한 코드 작성
                    pass
                elif "방어력_증가" in selected_item:
                    # 방어력 증가에 대한 코드 작성
                    pass
                
                # 아이템 사용 후 해당 아이템 삭제
                player_items.remove(selected_item)
                
            else:
                print("\n잘못된 입력입니다.")
        
        elif choice == "3":
            print("\n도망갑니다!")
            break
        
        else:
            print("\n잘못된 입력입니다.")
    
    has_rested = False  # 전투 후 휴식 가능
    has_visited_shop = False  # 전투 후 상점 방문 가능

def rest():
    global player_health, has_rested
    
    if has_rested:
        print("\n이미 휴식을 취했습니다. 몬스터와 전투 후에 한 번만 휴식할 수 있습니다.")
    else:
        print("\n==================================")
        print("             휴식하기              ")
        print("==================================\n")
        print("휴식을 취합니다.")
        player_health += 20  # 체력 회복량
        print("체력이 회복되었습니다. 현재 체력:", player_health)
        has_rested = True

def shop():
    global player_money, player_items, has_visited_shop
    
    if has_visited_shop:
        print("\n이미 상점에 방문했습니다. 몬스터와 전투 후에 한 번만 상점에 갈 수 있습니다.")
    else:
        print("\n==================================")
        print("              상점                 ")
        print("==================================\n")
        print("상점에 오신 것을 환영합니다!")
        print("보유한 돈:", player_money)
        print("구매 가능한 아이템 목록:")
        
        for i, item in enumerate(shop_items):
            print(str(i+1) + ". " + item["이름"] + " - 가격:", item["가격"])
        
        choice = input("\n구매할 아이템의 번호를 선택하세요 (뒤로 가려면 0을 입력하세요): ")
        
        if choice.isdigit() and int(choice) <= len(shop_items):
            selected_item = shop_items[int(choice) - 1]
            
            if player_money >= selected_item["가격"]:
                player_money -= selected_item["가격"]
                player_items.append(selected_item)
                print("\n" + selected_item["이름"] + "을(를) 구매하였습니다.")
            else:
                print("\n돈이 부족하여 구매할 수 없습니다.")
        elif choice == "0":
            print("\n상점에서 나갑니다.")
        else:
            print("\n잘못된 입력입니다.")
        
        has_visited_shop = True

# 메인 게임 루프
while True:
    print("\n==================================")
    print("           텍스트 RPG 게임          ")
    print("==================================\n")
    print("1. 몬스터와 전투하기")
    print("2. 휴식하기")
    print("3. 상점")
    print("4. 게임 종료")
    
    choice = input("\n원하는 기능을 선택하세요: ")
    
    if choice == "1":
        battle()
    elif choice == "2":
        rest()
    elif choice == "3":
        shop()
    elif choice == "4":
        print("\n게임을 종료합니다.")
        break
    else:
        print("\n잘못된 입력입니다. 다시 선택해주세요.")
