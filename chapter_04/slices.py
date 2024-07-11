nums = [item for item in range(1, 1_000_000+1)]
print(f'The first three items in the list are: {nums[:3]}')
half = int(len(nums)/2)
print(f'Three items from the middle of the list are: {nums[half:half+3]}')
print(f'The last three items in the list are: {nums[-3:]}')