import moment from 'moment';
export const initialState = [{ date: 'start', on: [6, 0], off: [21, 0] }];

export const reducer = (state, action) => {
  let newState;
  let newDate;

  switch (action.type) {
    case 'setPlan':
      return action.payload.map((el) => ({
        date: el.date,
        on: el.on,
        off: el.off,
      }));

    case 'setStartCycle':
      newState = [...state];
      newState[0].on = [action.payload[0], 0];
      newState[0].off = [action.payload[1], 0];
      return newState;

    case 'setDateCycle':
      newState = [...state];
      newState[action.payload.index].on = [action.payload.range[0], 0];
      newState[action.payload.index].off = [action.payload.range[1], 0];
      return newState;

    case 'changeDate':
      newState = [...state];
      newState[action.payload.index].date = action.payload.date.format(
        'YYYY-MM-DD'
      );
      return newState;

    case 'addCycle':
      if (state.length > 1) {
        newDate = moment(state[state.length - 1].date)
          .add(1, 'day')
          .format('YYYY-MM-DD');
      } else {
        newDate = moment().add(1, 'day').format('YYYY-MM-DD');
      }

      return [
        ...state,
        {
          date: newDate,
          on: [6, 0],
          off: [18, 0],
        },
      ];

    case 'deleteCycle':
      newState = [...state];
      newState.splice(action.payload.index, 1);
      return newState;

    default:
      return state;
  }
};
