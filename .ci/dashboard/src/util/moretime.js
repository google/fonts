import { timeInterval } from "d3-time";

export const utcQuarter = timeInterval(
  (date) => {
    date.setUTCDate(1);
    date.setUTCHours(0, 0, 0, 0);
  },
  (date, step) => {
    date.setUTCMonth(date.getUTCMonth() + 3 * step);
  },
  (start, end) => {
    return (
      (end.getUTCMonth() -
        start.getUTCMonth() +
        (end.getUTCFullYear() - start.getUTCFullYear()) * 12) /
      3
    );
  },
  (date) => {
    return date.getUTCMonth() / 3;
  }
);
