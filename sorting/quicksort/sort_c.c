#include <stdio.h>
#include <sys/time.h>
#include <time.h>
#include <stdlib.h>

#define min 0
#define max 1
#define pre 1000000


static double get_wall_seconds() {
  struct timeval tv;
  gettimeofday(&tv, NULL);
  double seconds = tv.tv_sec + (double)tv.tv_usec / 1000000;
  return seconds;
}

void random_list(double** lis, int size){
    *lis=(double*)malloc(size*sizeof(double));
    srand(time(NULL));   

    for (int i = 0; i < size; i++) {
        (*lis)[i] = (rand() % pre) / (double) pre * (max-min) + min;
    }
}


void cpy(double** l, double* l1, int size){
    *l=(double*)malloc(size*sizeof(double));
    for (int i = 0; i < size; i++) {
        (*l)[i] = l1[i];
    }
}

void merge(double* left, int leftLength, double* right, int rightLength, double** merged) {
    int i = 0, j = 0;
    int mergedLength = leftLength + rightLength;
    *merged = (double*)malloc(mergedLength * sizeof(double));

    int index = 0;
    while (i < leftLength && j < rightLength) {
        if (left[i] <= right[j]) {
            (*merged)[index] = left[i];
            i++;
        } else {
            (*merged)[index] = right[j];
            j++;
        }
        index++;
    }

    while (i < leftLength) {
        (*merged)[index] = left[i];
        i++;
        index++;
    }

    while (j < rightLength) {
        (*merged)[index] = right[j];
        j++;
        index++;
    }
}

void mergeSort(double* lis, int length) {
    if (length <= 1) {
        return;
    }

    int mid = length / 2;
    double* left = (double*)malloc(mid * sizeof(double));
    double* right = (double*)malloc((length - mid) * sizeof(double));

    for (int i = 0; i < mid; i++) {
        left[i] = lis[i];
    }
    for (int i = mid; i < length; i++) {
        right[i - mid] = lis[i];
    }

    mergeSort(left, mid);
    mergeSort(right, length - mid);

    merge(left, mid, right, length - mid, &lis);

    free(left);
    free(right);
}

void bubbleSort(double* arr, int n) {
    int i, j;
    double temp ;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int partition(double* arr, int lo, int hi) {
    double pivot = arr[(hi - lo) / 2 + lo];
    int i = lo - 1;
    int j = hi + 1;

    while (1) {
        do {
            i++;
        } while (arr[i] < pivot);

        do {
            j--;
        } while (arr[j] > pivot);

        if (i >= j)
            return j;

        double temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

void quickSort(double* arr, int lo, int hi) {
    if (lo >= 0 && hi >= 0 && lo < hi) {
        int p = partition(arr, lo, hi);
        quickSort(arr, lo, p);
        quickSort(arr, p + 1, hi);
    }
}


int main(int argc, char** args){
    int size = 50000;
    //int size=10;
    double* lis;
    double* l1;
    double start ;
    random_list(&lis, size);

    cpy(&l1,lis,size);

    start = get_wall_seconds(); 
    quickSort(l1, 0, size-1);
    printf("--- %lf seconds --- qsort\n", get_wall_seconds() - start);


    cpy(&l1,lis,size);
    start = get_wall_seconds(); 
    mergeSort(l1, size);
    printf("--- %lf seconds --- merge\n", get_wall_seconds() - start);


    cpy(&l1,lis,size);
    start = get_wall_seconds(); 
    bubbleSort(l1, size);
    printf("--- %lf seconds --- bubble\n", get_wall_seconds() - start);

    free(lis);
    free(l1);
    /*
    printf("\nSorted array: ");
    for (int i = 0; i < size; i++) {
        printf("%lf ", lis[i]);
    }
    printf("\n");*/


    return 0;
}