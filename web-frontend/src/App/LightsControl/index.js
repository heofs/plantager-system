import React, { useState, useEffect, useReducer } from 'react';
import { Slider, Button, Row, Col } from 'antd';
import { PlusCircleOutlined } from '@ant-design/icons';
import { useQuery, useMutation } from '@apollo/react-hooks';
import { GET_LIGHT_PLAN, UPDATE_LIGHT_PLAN } from 'graphql/light-plan';
import ConfirmationModal from './confirmation-modal';
import { initialState, reducer } from './plan-reducer';

const marks = {};
for (let x = 0; x <= 24; x++) {
  marks[x] = `${x}h`;
}

export const LightsControl = () => {
  const default_lights = [0, 24];
  const [lightPlan, dispatchPlan] = useReducer(reducer, initialState);
  const [dateCycles, setDateCycles] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);
  const { loading, data } = useQuery(GET_LIGHT_PLAN, {
    fetchPolicy: 'network-only',
  });
  const [updateLights] = useMutation(UPDATE_LIGHT_PLAN);

  const addCycle = () => {
    dispatchPlan({ type: 'addCycle' });
  };

  useEffect(() => {
    if (!loading && data && data.lightPlan) {
      dispatchPlan({ type: 'setPlan', payload: data.lightPlan.value });
    }
  }, [loading, data]);

  useEffect(() => {
    const dateCycles = [...lightPlan];
    dateCycles.shift();
    setDateCycles(dateCycles);
  }, [lightPlan]);

  return (
    <Row gutter={[8, 16]}>
      <Col span={24}>
        <h2 style={{ textAlign: 'center' }}>Set lights cycle</h2>
      </Col>
      <Col span={24}>
        <Slider
          range
          marks={marks}
          defaultValue={default_lights}
          max={24}
          dots={true}
          value={[lightPlan[0].on[0], lightPlan[0].off[0]]}
          onChange={(range) => {
            dispatchPlan({ type: 'setStartCycle', payload: range });
          }}
          disabled={loading}
        />
      </Col>
      {dateCycles.map((el, index) => {
        const planIndex = index + 1;
        return (
          <Col key={index} span={24}>
            <p>{el.date}</p>
            <Slider
              range
              marks={marks}
              defaultValue={default_lights}
              max={24}
              dots={true}
              value={[lightPlan[planIndex].on[0], lightPlan[planIndex].off[0]]}
              onChange={(range) => {
                dispatchPlan({
                  type: 'setDateCycle',
                  payload: { index: planIndex, range },
                });
              }}
            />
          </Col>
        );
      })}
      <Col span={24} flex="auto" style={{ textAlign: 'center' }}>
        <Button
          type="primary"
          shape="circle"
          icon={<PlusCircleOutlined />}
          size={'large'}
          onClick={addCycle}
        />
      </Col>
      <Col span={24}>
        <Button
          type="primary"
          block
          onClick={() => setModalVisible(true)}
          size={'middle'}
        >
          Save
        </Button>
      </Col>
      <ConfirmationModal
        lightPlan={lightPlan}
        modalVisible={modalVisible}
        setModalVisible={setModalVisible}
        onConfirm={() =>
          updateLights({
            variables: {
              lightPlan: lightPlan,
            },
          })
        }
      />
    </Row>
  );
};

export default LightsControl;
