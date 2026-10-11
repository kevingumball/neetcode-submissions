class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                res = mid
                break

            if nums[l] < nums[r]:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                if nums[mid] >= nums[l]:
                    if nums[mid] < target:
                        l = mid + 1
                    elif nums[mid] > target and target < nums[l]:
                        l = mid +1
                    else:
                        r = mid - 1
                else:
                    if target > nums[r]:
                        r = mid - 1
                    elif nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
        return res