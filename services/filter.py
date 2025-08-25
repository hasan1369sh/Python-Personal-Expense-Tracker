import datetime

def filtered_item(self, time_frame):
    now = datetime.datetime.now()
    today_date = now.date()
    result = []
    try:
        if time_frame == 'today':
            for transaction in self.transactions:
                trans_date = datetime.datetime.strptime(transaction.date, '%Y-%m-%d').date()
                if trans_date == today_date:
                    result.append(transaction)

        elif time_frame == 'current week':
            # شروع هفته: دوشنبه هفته جاری
            start_of_week = now - datetime.timedelta(days=now.weekday())
            start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
            end_of_week = now

            for transaction in self.transactions:
                trans_datetime = datetime.datetime.strptime(transaction.date, '%Y-%m-%d')
                if start_of_week <= trans_datetime <= end_of_week:
                    result.append(transaction)

        elif time_frame == 'current month':
            start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            end_of_month = now

            for transaction in self.transactions:
                trans_datetime = datetime.datetime.strptime(transaction.date, '%Y-%m-%d')
                if start_of_month <= trans_datetime <= end_of_month:
                    result.append(transaction)

        elif time_frame == 'range':
            from_str = input('From Date (YYYY-MM-DD): ')
            to_str = input('To Date (YYYY-MM-DD): ')
            from_date = datetime.datetime.strptime(from_str, '%Y-%m-%d')
            to_date = datetime.datetime.strptime(to_str, '%Y-%m-%d')
            to_date = to_date.replace(hour=23, minute=59, second=59)

            for transaction in self.transactions:
                trans_datetime = datetime.datetime.strptime(transaction.date, '%Y-%m-%d')
                if from_date <= trans_datetime <= to_date:
                    result.append(transaction)

        else:
            print("❌ Invalid time frame.")
    except Exception as e:
        print(f"❌ Error in filtering: {e}")
        return []

    return result

