def median(a, testing):
    if len(a) % 2 == 0:
        return 0.5 * (a[len(a) // 2 - 1] + a[len(a) // 2])
    else:
        return a[len(a) // 2]


def median_two_arrays(nums1,nums2,testing=False):
    # lena,lenb = len(nums1),len(nums2)
    if testing:
        print(median(nums1,testing),median(nums2,testing))
        print(nums1+nums2)
    return median(sorted(nums1 + nums2),testing)

nums1 = [1,3]
nums2 = [2]

print(median_two_arrays(nums1,nums2,True))