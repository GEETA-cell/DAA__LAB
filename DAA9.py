import math


def first_fit(items, capacity=1.0):
    bins = []          # Remaining space in each bin
    bin_contents = []  # Items stored in each bin

    for item in items:
        placed = False

        # Try to place the item in the first bin that has enough space
        for i, space in enumerate(bins):
            if space + 1e-9 >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break

        # If item cannot fit in any existing bin, create a new bin
        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    # Sort items from largest to smallest
    sorted_items = sorted(items, reverse=True)

    return first_fit(sorted_items, capacity)


def best_fit_decreasing(items, capacity=1.0):
    # Sort items from largest to smallest
    sorted_items = sorted(items, reverse=True)

    bins = []          # Remaining space
    bin_contents = []  # Items in each bin

    for item in sorted_items:

        best_idx = -1
        best_space = float('inf')

        # Find the bin that will have the least remaining space
        # after placing the item
        for i, space in enumerate(bins):

            if space + 1e-9 >= item:
                remaining = space - item

                if remaining < best_space:
                    best_space = remaining
                    best_idx = i

        # Place item in the best-fitting existing bin
        if best_idx >= 0:
            bins[best_idx] -= item
            bin_contents[best_idx].append(item)

        # Otherwise create a new bin
        else:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def display_bins(label, bins):

    print(f"\n{label}: {len(bins)} bins")

    for i, b in enumerate(bins, 1):

        used = sum(b)

        # Avoid displaying 0.9999999999999999
        used = round(used, 1)

        bar = '#' * int(used * 20)

        print(
            f"  Bin {i}: {[round(x, 1) for x in b]}"
            f" | Used: {used:.1f} "
            f"[{bar:<20}]"
        )


# --------------------------------------------------
# Input
# --------------------------------------------------

items = [
    0.5, 0.7, 0.3, 0.9, 0.2,
    0.6, 0.8, 0.4, 0.1, 0.5
]

capacity = 1.0


# --------------------------------------------------
# Lower bound
# --------------------------------------------------

total = sum(items)

lower_bound = math.ceil(total / capacity)


# --------------------------------------------------
# Display input information
# --------------------------------------------------

print(f"Items: {items}")
print(f"Capacity: {capacity}")
print(f"Sum of items: {total:.1f}")
print(f"Lower bound on bins: {lower_bound}")


# --------------------------------------------------
# Run algorithms
# --------------------------------------------------

ff_bins = first_fit(items, capacity)
ffd_bins = first_fit_decreasing(items, capacity)
bfd_bins = best_fit_decreasing(items, capacity)


# --------------------------------------------------
# Display results
# --------------------------------------------------

display_bins("First Fit (FF)", ff_bins)

display_bins(
    "First Fit Decreasing (FFD)",
    ffd_bins
)

display_bins(
    "Best Fit Decreasing (BFD)",
    bfd_bins
)


# --------------------------------------------------
# Summary
# --------------------------------------------------

print(
    f"\nSummary: Lower Bound={lower_bound}, "
    f"FF={len(ff_bins)}, "
    f"FFD={len(ffd_bins)}, "
    f"BFD={len(bfd_bins)}"
)