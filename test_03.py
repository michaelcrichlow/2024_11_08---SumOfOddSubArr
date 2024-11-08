from copy import deepcopy


def SumOfOddSubArr(arr: list[int]) -> int:
    if len(arr) == 0:
        return -1

    total = 0
    for i in range(len(arr)):
        last_index = len(arr) - (~((len(arr) - i) % 2) & 1)
        while last_index > 0:
            for j in range(i, last_index):
                total += arr[j]
            last_index -= 2

    return total


def sumOddLengthContiguousSubsequence(l: list[int]) -> int:
    # guard clause
    if len(l) == 1:
        return l[0]

    _l = deepcopy(l)
    _l.sort()
    local_array: list[int] = []
    total = 0

    for i in range(1, len(_l)):
        if _l[i - 1] == _l[i] - 1:
            if len(local_array) == 0:
                local_array.append(_l[i - 1])
                local_array.append(_l[i])
                continue
            else:
                local_array.append(_l[i])
                continue

        if len(local_array) != 0:
            if len(local_array) % 2 != 0:
                total += sum(local_array)

            local_array.clear()

    if len(local_array) != 0:
        if len(local_array) % 2 != 0:
            total += sum(local_array)

    return total


def main() -> None:
    print(SumOfOddSubArr([1, 4, 2, 5, 3]))  # 58
    print(sumOddLengthContiguousSubsequence([1, 4, 2, 5, 3]))  # 15


if __name__ == '__main__':
    main()


# sumOddLengthSubarrays([1,4,2,5,3]) => 58
# [1, 4, 2, 5, 3, 9, 7, 8]

# static int SumOfOddSubArr(int[] arr)
# {
#     int len = arr.Length;
#     if(len == 0)
#     {
#         return -1;
#     }
#     int sum = 0;
#     for(int i = 0; i < len; i++)
#     {
#         int lastIndex = len - (~((len - i) % 2) & 1);
#         while(lastIndex > 0)
#         {
#             for(int j = i; j < lastIndex; j++)
#             {
#                 sum += arr[j];
#             }
#             lastIndex -= 2;
#         }
#     }
#     return sum;
# }
