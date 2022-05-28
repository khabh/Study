#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
int orderCoffee();
int orderDesert();
void solveSecret();
int orderSweets();

int main() {
	int order, prices = 0,solve = 0;
	printf("어서 오세요 손님 ◆◆◆◆◆에 오신 것을 환영합니다.\n");
	while(1) {
		if (solve == 1)
			printf("◇허니듀크◇에 오신 걸 환영합니다\n");
		printf("무엇을 주문하시겠어요?\n\n");
		printf("┌────────────────────┐\n│ 1. 향긋한 커피     │\n│ 2. 달콤한 디저트   │\n│ 4. 이곳에 대한 정보│\n│ 5. 계산            │\n");
		if (solve == 1) {
			printf("│ 6. 허니듀크 과자   │\n");
		}
		printf("└────────────────────┘\n\n");
		scanf("%d", &order);
		getchar();

		if (order > 5 && order < 1) {
			if (order == 6 && solve ==1);
			else
				continue;
		}

		switch (order) {
		case 1: 
			prices += orderCoffee(); 
			break;
		case 2: 
			prices += orderDesert(); 
			break;
		case 3:
			if (solve == 0)
				printf("◆◆◆◆◆를 제대로 즐기고 싶다면 이곳에 대한 정보를 알아내세요.\n");
			else
				printf("허니듀크를 즐기고 계신가요?\n");

			getchar();
			break;
		case 4: 
			if (solve == 1) {
				printf("이곳은 허니듀크입니다 :)");
				getchar();
			}else {
				solveSecret();
				solve = 1;}
			break;
		case 5: 
			if (prices == 0) {
				printf("손님 아직 주문을 하지 않으셨어요^^\n\n");
				getchar();
				continue;
			}else {
				printf("\n네, 손님 총 %d원 결제되었습니다.", prices);
				getchar();
				printf("감사합니다. 다음에 또 방문해 주세요!\n");
				return 0;}
		case 6: 
			prices += orderSweets(); 
			break;
		}		
	}
	return 0;
}

int orderCoffee() {
	char size;
	int coffee, total=0;

	printf("\n▽원하는 커피를 선택해 주세요.▽\n");
	printf("┌──────────────┐\n│ 1. 아메리카노│\n│ 2. 카페라떼  │\n│ 3. 에스프레소│\n│ 4. 카푸치노  │\n│ 5. 카라멜라떼│\n│ 6. 바닐라라떼│\n│ 7. 카페모카  │\n└──────────────┘\n\n");
	scanf("%d", &coffee);
	getchar();

	printf("사이즈를 선택하세요.(S/M/L)\n");
	printf("정확하게 입력하지 않을 경우 기본 사이즈로 선택됩니다.");
	scanf("%c", &size);
	getchar();

	if (size == 'M' || size == 'm') {
		total += 500;
	}
	else if (size == 'L' || size == 'l') {
		total += 1000;
	}
	switch (coffee) {
	case 1: 
	case 2:
	case 3:
	case 4: total += 2500; break;
	case 5:
	case 6:
	case 7: total += 3500; break;
	default:
		printf("주문이 취소되었습니다.\n");
		return 0;
	}
	printf("주문하신 커피 나왔습니다!\n\n");
	getchar();
	return total;
}


int orderDesert() {
	int desert,price;
	printf("\n▽원하는 디저트를 선택해 주세요.▽\n");
	printf("┌──────────────┐\n│ 1. 벨벳케이크│\n│ 2. 초코칩쿠키│\n│ 3. 생크림와플│\n│ 4. 하트프레첼│\n└──────────────┘\n\n");
	scanf("%d", &desert);
	getchar();

	switch (desert) {
	case 1: price = 7500; break;
	case 2: price = 3500; break;
	case 3: 
	case 4:  price = 4000; break;
	default: 
		printf("주문이 취소되었습니다.\n");
		return 0;
	}
	printf("주문하신 디저트 나왔습니다!\n");
	getchar();
	return price;
}


void solveSecret() {
	int answer;
	printf("이곳에 대한 정보를 얻기 위해서는 아주 아주 어려운 문제를 풀어야 합니다.\n");
	while (1) {
		printf("1+1은?");
		scanf("%d", &answer);
		getchar();
		if (answer == 2) {
			printf("\n정답입니다.\n정보 - 이 가게의 주인은 암브로시우스 플룸입니다.\n");
			getchar();
			break;
		}
		else
			printf("문제가 너무 어려웠나요?다시 도전해 보세요!\n");
	}
	while (1) {
		printf("첫번째 문제를 맞히셨군요, 이번엔 더 어려운 문제가 준비되어 있습니다.\n2 * 2 는?");
		scanf("%d", &answer);
		getchar();

		if (answer == 4) {
			printf("\n정답입니다.\n정보 - 이 가게는 사실 호그와트와 연결되어 있습니다.\n");
			getchar();
			break;
		}
		else
			printf("문제가 너무 어려웠나요?다시 도전해 보세요!\n");
	}
	while (1) {
		printf("마지막 문제입니다\n(e^(ㅠi) + cos(ㅠ)+isin(ㅠ)) * 0 은?");
		scanf("%d", &answer);
		getchar();
		if (answer == 0) {
			printf("\n정답입니다.\n");
			printf("축하드려요 드디어 수수께끼를 푸셨군요!\n이곳은 환상적인 과자들이 판매되고 있는 허니듀크입니다!\n");
			getchar();
			break;
		}
		else
			printf("문제가 너무 어려웠나요?다시 도전해 보세요!\n");
	}
}


int orderSweets() {
	int sweets,price;
	printf("\n▽원하는 상품을 골라 주세요▽\n");

	printf("┌──────────────────┐\n│ 1. Treacle fudge │\n│ 2. Fever Fudge   │\n│ 3. Pixie Puffs   │\n│ 4. Butter Bear   │\n│ 5. Sugar Quills  │\n└──────────────────┘\n\n");
	scanf("%d", &sweets);
	getchar();

	switch (sweets) {
	case 1:
		price = 20000;
		printf("주문하신 당밀퍼지 나왔습니다.\n초콜릿과 당밀이 들어간 끈적한 간식입니다\n\n");
		break;
	case 2:
		price = 8900;
		printf("주문하신 발열 사탕 나왔습니다.\n열이 펄펄 끓게 만드는 간식으로 꾀병용 과자라고도 불린답니다.\n\n");
		break;
	case 3:
		price = 40000;
		printf("주문하신 픽시 퍼프 나왔습니다.\n마법사 세계의 아침용 시리얼로 우유랑 아주 잘 어울린답니다.\n\n");
		break;
		
	case 4:
		price = 10000;
		printf("주문하신 버터 맥주 나왔습니다.\n호그와트 학생들에게 인기가 많은 무알콜 음료입니다.\n\n");
		break;
	case 5:
		price = 8000;
		printf("주문하신 설탕 깃펜 나왔습니다.\n수업 중 몰래 사탕을 먹을 수 있어서 학생들 사이에 인기를 끌고 있습니다\n\n");
		
		
	}

	getchar();
	return price;
}
