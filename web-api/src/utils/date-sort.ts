import dayjs from 'dayjs';

export const sortArrayByDate = (a: Cycle, b: Cycle): number => {
  if (dayjs(a.date) > dayjs(b.date)) return 1;
  if (dayjs(b.date) > dayjs(a.date)) return -1;
  return 0;
};
